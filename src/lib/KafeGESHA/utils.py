from lib.KafeMATH.funciones import exp, pow_, sqrt, log, math_abs
from  lib.KafeNUMK.funciones import shape,dot,dot_matrix,zeros,zeros_matrix

def escalonada(x):
    return 1 if x >= 0 else 0

def sigmoide(x):
    return 1 / (1 + exp(-x))

def relu(x):
    return x if x > 0 else 0

def identidad(x):
    return x

def tanh(x):
    e_pos = exp(x)
    e_neg = exp(-x)
    return (e_pos - e_neg) / (e_pos + e_neg)

def softmax(vec):
    """Softmax aplicada a un vector de valores"""
    exp_vec = [exp(x) for x in vec]
    suma = sum(exp_vec)
    return [x / suma for x in exp_vec]

def activar(nombre: str):
    funciones = {
        "escalonada": escalonada,
        "sigmoide": sigmoide,
        "relu": relu,
        "tanh": tanh,
        "identidad": identidad,
    }
    if nombre not in funciones:
        raise ValueError(f"Función de activación '{nombre}' no soportada.")
    return funciones[nombre]

#=======================OPTIMIZADORES========================================



class Optimizer:
    def step(self, params, grads):
        raise NotImplementedError("Debe implementarse en subclases.")

class SGD(Optimizer):
    def __init__(self, lr=0.01):
        self.lr = lr

    def step(self, params, grads):
        return [p - self.lr * g for p, g in zip(params, grads)]

class RMSprop(Optimizer):
    def __init__(self, lr=0.001, rho=0.9, epsilon=1e-8):
        self.lr = lr
        self.rho = rho
        self.epsilon = epsilon
        self.cache = None

    def step(self, params, grads):
        if self.cache is None:
            self.cache = [0 for _ in grads]
        new_params = []
        for i in range(len(params)):
            self.cache[i] = self.rho * self.cache[i] + (1 - self.rho) * pow_(grads[i], 2)
            update = self.lr * grads[i] / (sqrt(self.cache[i]) + self.epsilon)
            new_params.append(params[i] - update)
        return new_params

class Adam(Optimizer):
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.lr = lr
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m = None
        self.v = None
        self.t = 0

    def step(self, params, grads):
        if self.m is None:
            self.m = [0 for _ in grads]
            self.v = [0 for _ in grads]
        self.t += 1
        new_params = []
        for i in range(len(params)):
            self.m[i] = self.beta1 * self.m[i] + (1 - self.beta1) * grads[i]
            self.v[i] = self.beta2 * self.v[i] + (1 - self.beta2) * pow_(grads[i], 2)

            m_hat = self.m[i] / (1 - pow_(self.beta1, self.t))
            v_hat = self.v[i] / (1 - pow_(self.beta2, self.t))

            update = self.lr * m_hat / (sqrt(v_hat) + self.epsilon)
            new_params.append(params[i] - update)
        return new_params

class AdamW(Adam):
    def __init__(self, lr=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, weight_decay=0.01):
        super().__init__(lr, beta1, beta2, epsilon)
        self.weight_decay = weight_decay

    def step(self, params, grads):
        updated_params = super().step(params, grads)
        return [p - self.lr * self.weight_decay * p for p in updated_params]


#=======================Funciones de Perdida =======================


def mean_squared_error(y_true, y_pred):
    errors = [pow_(yt - yp, 2) for yt, yp in zip(y_true, y_pred)]
    return sum(errors) / len(errors)


def mean_absolute_error(y_true, y_pred):
    errors = [math_abs(yt - yp) for yt, yp in zip(y_true, y_pred)]
    return sum(errors) / len(errors)


def binary_cross_entropy(y_true, y_pred, epsilon=1e-8):
    loss = [
        -(yt * log(yp + epsilon) + (1 - yt) * log(1 - yp + epsilon))
        for yt, yp in zip(y_true, y_pred)
    ]
    return sum(loss) / len(loss)


def categorical_cross_entropy(y_true, y_pred, epsilon=1e-8):
    loss = [
        -sum([yt_i * log(yp_i + epsilon) for yt_i, yp_i in zip(yt, yp)])
        for yt, yp in zip(y_true, y_pred)
    ]
    return sum_(loss) / len(loss)


def sparse_categorical_cross_entropy(y_true, y_pred, epsilon=1e-8):
    loss = [-log(yp[int(yt)] + epsilon) for yt, yp in zip(y_true, y_pred)]
    return sum(loss) / len(loss)


def obtener_loss(nombre: str):
    funciones = {
        "mse": mean_squared_error,
        "mae": mean_absolute_error,
        "bce": binary_cross_entropy,
        "categorical_crossentropy": categorical_cross_entropy,
        "sparse_categorical_crossentropy": sparse_categorical_cross_entropy,
    }
    if nombre not in funciones:
        raise ValueError(f"Función de pérdida '{nombre}' no soportada.")
    return funciones[nombre]


#======================Derivadas Backpropagation ====================

def mse(y_true, y_pred):
    n = len(y_true)
    return sum([pow_((yt - yp), 2) for yt, yp in zip(y_true, y_pred)]) / n

def d_mse(y_true, y_pred):
    n = len(y_true)
    return [2 * (yp - yt) / n for yt, yp in zip(y_true, y_pred)]

'''Binary Cross-Entropy con Sigmoide en output '''

def binary_crossentropy(y_true, y_pred):
    n = len(y_true)
    loss = 0
    for yt, yp in zip(y_true, y_pred):
        loss += - (yt * log(yp) + (1 - yt) * log(1 - yp))
    return loss / n

def d_binary_crossentropy(y_true, y_pred):
    n = len(y_true)
    return [((yp - yt) / (yp * (1 - yp))) / n for yt, yp in zip(y_true, y_pred)]

'''Categorical Cross-Entropy con softmax en output '''

def categorical_crossentropy(y_true, y_pred):
    n = len(y_true)
    total_loss = 0
    for yt, yp in zip(y_true, y_pred):
        total_loss += -sum([yt_i * log(yp_i) for yt_i, yp_i in zip(yt, yp)])
    return total_loss / n

def d_categorical_crossentropy(y_true, y_pred):
    # y_true y y_pred son listas de vectores
    n = len(y_true)
    grad = []
    for yt, yp in zip(y_true, y_pred):
        grad.append([yp_i - yt_i for yt_i, yp_i in zip(yt, yp)])  # derivada del softmax + crossentropy
    return grad

''' MAE '''
def mae(y_true, y_pred):
    n = len(y_true)
    return sum([abs_(yt - yp) for yt, yp in zip(y_true, y_pred)]) / n

def d_mae(y_true, y_pred):
    n = len(y_true)
    return [1 / n if yp > yt else -1 / n for yt, yp in zip(y_true, y_pred)]


#=================== BackPropagation ===============================

def backprop(loss_grad, activaciones, pesos, y_true, lr=0.01, act_grads=[]):
    deltas = []
    
    # Última capa
    delta = loss_grad(y_true, activaciones[-1])  # dL/dy
    deltas.append(delta)


    for i in range(len(pesos)-1, 0, -1):
        act_grad = act_grads[i-1](activaciones[i])
        peso = pesos[i]
        delta = [act_grad[j] * sum([peso[k][j] * deltas[-1][k] for k in range(len(deltas[-1]))]) for j in range(len(act_grad))]
        deltas.append(delta)

    deltas = deltas[::-1]  

    # Actualizar pesos
    for i in range(len(pesos)):
        for j in range(len(pesos[i])):        
            for k in range(len(pesos[i][j])): 
                pesos[i][j][k] -= lr * deltas[i][j] * activaciones[i][k]
