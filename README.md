# ☕️ KAFE — Kafe Deep Learning Language

**KAFE** es un lenguaje de programación diseñado como un DSL (Domain-Specific Language) para facilitar el aprendizaje de conceptos de *Deep Learning*, estructuras funcionales y procesamiento simbólico. Realizado por 4
Estudiantes de ciencias de la computacion E inteligencia artificial de la Universidad Sergio Arboleda.

**KAFE** sigue en etapa de desarrollo, hay cosas por pulir y arreglar pero toda persona interesada en agregar su granito de Kafe al proyecto es bienvenida.

> 🍰 "The people who are crazy enough to think they can change the world are the ones who do."  Steve Jobs

---

##  Características principales

- 🧠 Inspirado en lenguajes funcionales
- 🔁 Soporte para funciones lambda, currificación y de alto nivel 
- 🧮 Librería `KafeMatrix` tipo NumPy para álgebra lineal
- 📊 Librería `Plot` tipo Matplotlib para visualización
- 🧠 Librería `KAFE GESHA` Libreria para manejo de redes neuronales y deep learning
- 🧮 Librería `MATH` Libreria de utilidades matematicas
- 📊 Librería `FILES` Libreria para manejo de archivos
- 🧠 Librería `PARDOS` Libreria para manejo de archivos CSV
- ⚙️ Construido con ANTLR + Python 
- 🖥️ Aplicativo WEB  (Compilador en linea)
- 🔁  TESTS Automatizados

---

## 🛠️ Instalación

Puedes ejecutar **KAFE** localmente desde tu terminal. Actualmente, la versión web no está disponible para uso local, pero puedes trabajar perfectamente con KAFE como lenguaje de scripting desde tu entorno.
Tenemos dos opciones que puedes utilizar la primera es instalar manualmente todos los requisitos que necesita el proyecto para su ejecucion: 

### ✅ Requisitos

Asegúrate de tener instalados los siguientes paquetes antes de iniciar:

- **Python** `>= 3.10`
- **ANTLR 4** runtime para Python
- **Git**
- **Pytest** (para pruebas automatizadas)

---

### 🧪 Opción alternativa: Entorno reproducible con **Nix Flake**

Si prefieres evitar instalar dependencias manualmente que recomendamos esta opcion, puedes utilizar nuestro entorno preconfigurado con **Nix Flake**. Este entorno contiene todas las herramientas necesarias para compilar y ejecutar KAFE, incluyendo:

- Python 3.10+
- ANTLR 4 runtime
- OpenJDK
- Git
- Pytest

#### 🚀 Usar KAFE con Nix

### 🐧 Instalación de Nix en **Linux**

1. Abre tu terminal.
   
2. Ejecuta el siguiente comando para instalar Nix:
```bash
curl -L https://nixos.org/nix/install | sh
```
3.Una vez instalado, reinicia tu terminal o ejecuta:
```bash
. ~/.nix-profile/etc/profile.d/nix.sh
```
4. Habilita los flakes:
```bash
mkdir -p ~/.config/nix
nano ~/.config/nix/nix.conf
```
Y dentro del archivo activa lo siguiente : 
```bash
experimental-features = nix-command flakes
```

### 🍎 Instalación de Nix en macOS (Intel / Apple Silicon)

1. Abre la aplicación Terminal.
   
2. Ejecuta el siguiente comando:
```bash
curl -L https://nixos.org/nix/install | sh
```
3. En Apple Silicon (M1/M2/M3), si encuentras problemas, puedes ejecutar Terminal usando Rosetta o configurar el entorno adecuadamente para tu arquitectura.

4. Activa flakes igual que en Linux

✅ Una vez Nix esté listo, puedes iniciar el entorno de desarrollo con:
```bash
nix develop
```


### 📥 Clonar e instalar

Puedes comenzar a trabajar con **KAFE** clonando el repositorio oficial y ejecutando la instalación manual o mediante Nix.

```bash
git clone https://github.com/TuUsuario/KAFE.git
cd KAFE
```
📺 **Tutorial en Video**

Una vez que tengas todo instalado, puedes seguir el siguiente video donde se explica de forma visual y clara cómo usar **KAFE** desde tu terminal, ejecutar pruebas, y trabajar de manera más sencilla y eficiente con el lenguaje.

🔗 [Ver el video tutorial](ENLACE_AQUI)

