import React, { useState } from "react";


export default function Docs() {
  const [section, setSection] = useState("intro"); 

  return (
    <div className="docs-layout">
      <aside className="docs-sidebar">
        <h2 className="sidebar-title">KAFE Docs</h2>
        <nav className="sidebar-nav">
          <details open>
            <summary>Getting Started</summary>
            <ul>
              <li><a onClick={() => setSection("intro")}>Introduction</a></li>
              <li><a onClick={() => setSection("quick")}>Quick Start Guide</a></li>
            </ul>
          </details>
          <details open>
            <summary>Lenguaje KAFE <span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("comentarios")}>Comentarios</a></li>
              <li><a onClick={() => setSection("variables")}>Variables y Tipos</a></li>
              <li><a onClick={() => setSection("operadores-matemáticos")}>Operadores Matemáticos</a></li>
              <li><a onClick={() => setSection("listas-matrices")}>Listas y Matrices</a></li>
              <li><a onClick={() => setSection("condicionales")}>Condicionales</a></li>
              <li><a onClick={() => setSection("bucles")}>Bucles</a></li>
              <li><a onClick={() => setSection("funciones")}>Funciones</a></li>
              <li><a onClick={() => setSection("currificables")}>Funciones Currificables</a></li>
              <li><a onClick={() => setSection("alto-nivel")}>Funciones de Alto Nivel</a></li>
              <li><a onClick={() => setSection("recursivas")}>Funciones Recursivas</a></li>
            </ul>
          </details>
          <details open>
            <summary>Numk <span className="badge">New</span></summary>
            <ul></ul>
          </details> 
          <details open>
            <summary>Plot<span className="badge">New</span></summary>
            <ul></ul>
          </details> 
          <details open>
            <summary>Math <span className="badge">New</span></summary>
            <ul></ul>
          </details> 
          <details open>
            <summary>Files <span className="badge">New</span></summary>
            <ul></ul>
          </details> 
          <details open>
            <summary>Pardos<span className="badge">New</span></summary>
            <ul></ul>
          </details>
          <details open>
            <summary>GeshaDeep<span className="badge">New</span></summary>
            <ul></ul>
          </details>  
        </nav>
      </aside>

      <main className="docs-content">
        {section === "intro" && (
          <section>
            <h1>Introducción</h1>
              <p>
                <strong>KAFE</strong> es un lenguaje de programación diseñado para la comunidad académica. 
                <em>Domain-Specific Language</em> (DSL) enfocado en el desarrollo de redes neuronales, con una orientación 
                funcional que permite el uso de funciones currificables, composición funcional y estructuras declarativas.
              </p>
              <p>
                Este lenguaje ha sido creado para facilitar el aprendizaje de conceptos fundamentales en programación 
                y bases de <strong>Deep Learning</strong>. Nuestro objetivo es proporcionar una herramienta simple, clara 
                y educativa que promueva una comprensión profunda del funcionamiento interno de los modelos neuronales.
              </p>
              <p>
              <strong>KAFE</strong> es desarrollado por un equipo de cuatro estudiantes de Ciencias de la Computación e Inteligencia Artificial, 
                con el propósito de contribuir al ecosistema educativo. Nos alegra que estés explorando y utilizando este proyecto.
              </p>
              <p>
                Inicialmente, <strong></strong> está pensado para ejecutarse en este entorno web: puedes escribir tu código, compilarlo, 
                descargar los archivos generados y, si deseas continuar más adelante, simplemente vuelve a subirlos para 
                seguir trabajando donde lo dejaste.
              </p>
             
            </section>
        )}
        {section === "quick" && (
          <section>
            <h2>Guía Rápida para Empezar</h2>
             <p> ¡Bienvenido a <strong>KAFE</strong>, tu entorno de desarrollo online para aprender y experimentar con programación funcional de forma sencilla e intuitiva
              Este compilador en línea te permite escribir, ejecutar y visualizar código sin necesidad de instalar nada. Solo necesitas iniciar sesión y comenzar a programar.
              Estamos encantados de que estés explorando <strong>KAFE</strong>. Para ayudarte a comenzar, copia el siguiente fragmento de código, pégalo en el editor y haz clic en "Ejecutar". Verifica que todo funcione correctamente:
            </p>
            <pre>{`import NUMK;\nINT a = 5;`}</pre><br></br>
          </section>
        )}
  
{section === "comentarios" && (
  <section>
    <h2>Comentarios</h2>

    <p>
      En <strong>KAFE</strong>, los comentarios permiten incluir anotaciones o explicaciones dentro del código,
      sin que afecten su ejecución. Son útiles para describir la intención del código, explicar secciones complejas
      o dejar recordatorios.
    </p>

    <h3>Tipos de Comentarios</h3>
    <br />
    <p><strong>Comentario de una sola línea</strong></p>
    <p>
      Se escribe iniciando la línea con el símbolo <code>--</code>. Todo lo que siga en esa línea será ignorado por el compilador.
    </p>

    <pre><code>{`--Este es un comentario de una línea

INT x = 10; --También puede ir al final de una línea de código`}</code></pre>
      <br />

    <p><strong>Comentario de múltiples líneas</strong></p>
    <p>
      Se delimita entre <code>-&gt;</code> y <code>&lt;-</code>, y puede ocupar varias líneas.
    </p>

    <pre><code>{`->
Este es un comentario
de varias líneas en KAFE.
<-
INT y = x + 5;`}</code></pre>
<br />

    <h3>Notas</h3>
    <ul>
      <br />
      <li>Los comentarios no afectan la ejecución ni el resultado del programa.</li>
      <br />
      <li>Se recomienda usarlos para mejorar la legibilidad del código.</li>
    </ul>
  </section>
)}

        {section === "variables" && (
          <section>
            <h1>Variables y Tipos</h1>
            <p>En KAFE, las listas son estructuras de datos muy versátiles que te permiten almacenar múltiples elementos del mismo tipo, ya sea números, cadenas, booleanos, o incluso otras listas.
            Esto significa que puedes representar desde colecciones simples hasta estructuras de datos complejas como matrices o listas multidimensionales.</p><br></br>

            <h1>Enteros</h1>
            <p>
              Para declarar un número entero, se utiliza el tipo <code>INT</code>. Los enteros pueden ser positivos o negativos, y se definen de la siguiente manera:
            </p>
            <pre><code>INT a = 5;</code></pre><br></br>
            <h1>Booleanos</h1>
            <p>
              Si deseas trabajar con valores booleanos (verdadero o falso), se utiliza el tipo <code>BOOL</code>. Es útil para controlar flujos lógicos, condiciones y ciclos:
            </p>
            <pre><code>BOOL b = True;</code></pre><br></br>
            <h1>Strings</h1>
            <p>
              Las cadenas de texto se representan con el tipo <code>STR</code>. Puedes usar tanto comillas simples como dobles para definirlas. Ambas son equivalentes:
            </p>
            <pre><code>STR nombre_de_tu_string = 'Hola este es un String';</code></pre><br></br>
            <h1>Flotantes</h1>
            <p>
              Para trabajar con números reales o decimales, se utiliza el tipo <code>FLOAT</code>. Este tipo es ideal para representar valores con parte fraccionaria, como porcentajes, promedios o resultados matemáticos más precisos:
            </p>
            <pre><code>FLOAT e = 234.234;</code></pre><br></br>

            <p>
              Recuerda que todas las instrucciones en KAFE deben finalizar con punto y coma (<code>;</code>). Además, el lenguaje es sensible a mayúsculas y minúsculas, así que <code>True</code> no es  <code>true</code>.
            </p>
          </section>
        )}

        {section === "operadores-matemáticos" && (
          <section>
            <h2>Operaciones Matemáticas</h2>

            <p>
              En <strong>KAFE</strong>, puedes realizar operaciones matemáticas básicas utilizando los operadores estándar.
              Estas operaciones funcionan con valores de tipo <code>INT</code> y <code>FLOAT</code>.
            </p>

            <br />

            <h3>Operadores Aritméticos</h3>
            <br />
            <ul>
              <li><code>+</code> Suma</li>
              <li><code>-</code> Resta</li>
              <li><code>*</code> Multiplicación</li>
              <li><code>/</code> División</li>
              <li><code>^</code> Potencia</li>
              <li><code>%</code> Módulo</li>
            </ul>

            <br />

            <h3>Ejemplos</h3>
            <br />
            <pre><code>{
`show(5 + 4 * 2);       -- 13
show((5 + 4) * 2);     -- 18
show(5 ^ 2 * 2);       -- 50
show(-3 - -3);         -- 0
show(5 % 4);           -- 1`}</code></pre>

            <br />

            <h3>Notas</h3>
            <br />
            <ul>
              <li>Se respeta la precedencia de operadores: <code>*</code>, <code>/</code>, <code>^</code> antes que <code>+</code> y <code>-</code>.</li>
              <br />
              <li>Usa paréntesis <code>()</code> para modificar el orden de evaluación.</li>
              <br />
              <li>El operador <code>^</code> se usa para elevar un número a una potencia.</li>
              <br />
              <li>El operador <code>%</code> devuelve el residuo de una división.</li>
            </ul>
          </section>
        )}


        {section === "listas-matrices" && (
             <section style={{ lineHeight: "1.75" }}>
            <h1>Listas y Matrices</h1>

        <p>En KAFE, las listas son estructuras de datos muy versátiles que te permiten almacenar múltiples elementos del mismo tipo, ya sea números, cadenas, booleanos, o incluso otras listas.
        Esto significa que puedes representar desde colecciones simples hasta estructuras de datos complejas como matrices o listas multidimensionales.</p>

              <pre><code>List[INT] f = [];</code></pre>

              <p>También puedes inicializarlas directamente:</p>
              <pre><code>List[BOOL] g = [True, False, True];</code></pre>

              <p>Para estructuras más complejas, puedes anidar listas y crear matrices:</p>
              <pre><code>List[List[FLOAT]] h = [[234.234, 532.32], [234.4], []];</code></pre>

              <p>Una matriz bien formada puede verse así:</p>
              <pre><code>{`List[List[INT]] matriz = [
            [234, 234],
            [2341, 1234]
          ];`}</code></pre>

              <p>La sintaxis permite mucha flexibilidad:</p>
              <pre><code>{`List[INT] numeros = [1, 2, 3];
          List[STR] letras = ["a", "b"];
          List[BOOL] flags = [True];
          List[List[List[STR]]] cadenas = [];`}</code></pre>

              <p>Para mostrar el contenido de una lista:</p>
              <pre><code>{`show(numeros);
          show(cadenas);`}</code></pre>

              <p>Puedes agregar elementos dinámicamente con <code>append()</code>:</p>
              <pre><code>{`append(numeros, 99);
          append(letras, "z");
          append(flags, False);
          append(cadenas, [[["asdf"]]]);`}</code></pre>

              <p>Y mostrar los cambios:</p>
              <pre><code>{`show(numeros);
          show(letras);
          show(flags);
          show(cadenas);`}</code></pre>

              <p>Eliminar elementos se hace con <code>remove()</code>:</p>
              <pre><code>{`remove(numeros, 2);
          remove(letras, "a");`}</code></pre>

              <p>Verifica el resultado:</p>
              <pre><code>{`show(numeros);
          show(letras);`}</code></pre>

              <p>Para conocer la longitud de una lista:</p>
              <pre><code>show(len(numeros));</code></pre>

              <p>
                También puedes acceder a cualquier elemento por su índice, y modificarlo directamente:
              </p>
              <pre><code>{`List[INT] number = [1, 2, 3];
          List[STR] hola = ["h", "o"];
          List[List[List[BOOL]]] booleanos = [[[True, False]]];

          show(booleanos);
          show(number);
          show(hola);

          hola[0] = "f";
          number[0] = 100;
          booleanos[0] = [[False]];

          show(booleanos);
          show(number);
          show(hola);`}</code></pre>
  </section>
)}
        {section === "condicionales" && (
          <section>
            <h2>Condicionales</h2>

            <p>
              En <strong>KAFE</strong>, las estructuras condicionales permiten ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones. 
              Se utilizan las palabras clave <code>if</code>, <code>elif</code> y <code>else</code>, seguidas de dos puntos <code>:</code> y un bloque indentado.
            </p>

            <br />

            <h3>Sintaxis</h3>
            <br />
            <ul>
              <li><code>if (condición) :</code> — Ejecuta el bloque si la condición es verdadera.</li>
              <li><code>elif (condición) :</code> — Evalúa una condición adicional si el <code>if</code> fue falso.</li>
              <li><code>else :</code> — Ejecuta el bloque si ninguna condición previa fue verdadera.</li>
            </ul>

            <br />

            <h3>Ejemplo Completo</h3>
            <br />
            <pre><code>{
`INT edad = 25;
BOOL tieneLicencia = True;
INT puntos = 3;

if (edad >= 18) :
    if (tieneLicencia) :
        if (puntos < 5) :
            show("Puede conducir con normalidad");
        ; else :
            show("Puede conducir pero debe tener precaución");
        ;
    ; else :
        show("No puede conducir, no tiene licencia");
    ;
; else :
    if (edad >= 16) :
        show("Puede conducir con permiso de aprendizaje");
    ; else :
        show("Es menor de edad, no puede conducir");
    ;
;`}</code></pre>

            <br />

            <h3>Notas</h3>
            <br />
            <ul>
              <li>Las condiciones van entre paréntesis: <code>if (condición)</code>.</li>
              <br />
              <li>Los bloques se delimitan por indentación y deben terminar con <code>;</code>.</li>
              <br />
              <li>Se permiten condicionales anidados para tomar decisiones complejas.</li>
              <br />
              <li>Las cadenas se pueden mostrar usando <code>show("mensaje");</code>.</li>
            </ul>
          </section>
        )}

        {section === "bucles" && (
          <section>
              <h1 className="text-2xl font-bold mb-4">Bucles en KAFE</h1>

                  <p className="mb-4">
                    En <strong>KAFE</strong>, los bucles permiten repetir bloques de código mientras se cumplan ciertas condiciones. Existen dos estructuras principales:
                    <code>while</code> y <code>for</code>, cada una adaptada a diferentes tipos de tareas repetitivas.
                  </p>

                  <h2 className="text-xl font-semibold mt-6 mb-2">Bucle <code>while</code></h2>

                  <p className="mb-4">
                    El bucle <code>while</code> evalúa una condición antes de ejecutar su bloque. Si la condición es verdadera,
                    se ejecuta el contenido indentado hasta que la condición deje de cumplirse. Es ideal para situaciones donde
                    no se conoce de antemano cuántas veces se repetirá el ciclo.
                  </p>

                  <h3 className="text-lg font-medium mb-2">Sintaxis básica</h3>
                  <pre><code>{`while (condición):
                // instrucciones
            ;`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 1: Contador simple</h3>
                  <p>
                    En este ejemplo, una variable <code>i</code> se incrementa de 0 a 4, mostrando cada valor con <code>show</code>.
                  </p>
                  <pre><code>{`INT i = 0;
            while (i < 5):
                show(i);
                i = i + 1;
            ;`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 2: Comparación de dos variables</h3>
                  <p>
                    Aquí se demuestra cómo el ciclo <code>while</code> puede manejar múltiples condiciones lógicas para decidir si continuar.
                  </p>
                  <pre><code>{`INT a = 0;
            INT b = 5;
            while (a < b && b > 0):
                show(a);
                a = a + 1;
            ;`}</code></pre>

                  <h2 className="text-xl font-semibold mt-8 mb-2">Bucle <code>for</code></h2>

                  <p className="mb-4">
                    El bucle <code>for</code> es usado para iterar sobre secuencias como listas, rangos, u otras colecciones. Su sintaxis es más compacta
                    y legible cuando sabes cuántas veces deseas repetir una tarea.
                  </p>

                  <h3 className="text-lg font-medium mb-2">Sintaxis básica</h3>
                  <pre><code>{`for (elemento in colección):
                // instrucciones
            ;`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 1: Iterar sobre una lista de cadenas</h3>
                  <p>
                    Se recorre una lista de letras y se imprime cada una. Es una forma directa y clara de procesar secuencias.
                  </p>
                  <pre><code>{`List[STR] letras = ['K', 'A', 'F', 'E'];
            for (l in letras):
                show(l);
            ;`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 2: Rango descendente con <code>range</code></h3>
                  <p>
                    KAFE soporta la función <code>range(inicio, fin, paso)</code> para crear listas de números. En este caso se genera una
                    lista descendente desde 0 hasta -9 con paso -1.
                  </p>
                  <pre><code>{`List[INT] a = range(0, -10, -1);

            show(a);`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 3: Iteración sobre un rango</h3>
                  <p>
                    Puedes iterar directamente sobre un <code>range</code> en el bucle <code>for</code>. Este es el método más común para repeticiones fijas.
                  </p>
                  <pre><code>{`for(i in range(0, 10)):
                show(i);
            ;`}</code></pre>

                  <h3 className="text-lg font-medium mt-6 mb-2">Ejemplo 4: Rango corto</h3>
                  <p>
                    Cuando solo necesitas un número fijo de repeticiones (por ejemplo, 4 veces), puedes usar simplemente <code>range(4)</code>.
                  </p>
                  <pre><code>{`for(i in range(4)):
                show(i);
            ;`}</code></pre>

                  <p className="mt-6">
                    Estas estructuras de bucle son fundamentales para controlar el flujo de ejecución repetitiva en KAFE.
                    Su sintaxis está inspirada en lenguajes modernos pero simplificada para mantener claridad en contextos educativos.
                  </p>
          </section>
        )}
        {section === "funciones" && (
          <section>
            <h2>Funciones</h2>

            <p>
              En <strong>KAFE</strong>, las funciones permiten encapsular lógica reutilizable. 
              Se definen usando la palabra clave <code>drip</code>, seguidas del nombre de la función, sus parámetros con tipo, 
              el operador <code>=&gt;</code>, el tipo de retorno, y finalmente el cuerpo de la función.
            </p>

            <br />

            <h3>Sintaxis Básica</h3>
            <br />
            <pre><code>{`drip nombreFuncion (param1: TIPO, param2: TIPO) => TIPO_RETORNO :
            // cuerpo de la función
            return valor;
        ;`}</code></pre>

            <br />

            <h3>Ejemplo</h3>
            <br />
            <pre><code>{
`INT a = 9;
INT b = 6;

drip suma (a: INT, b: INT) => INT :
  return a + b;
;

show(suma(a, b));  -- Imprime 15`}</code></pre>

            <br />

            <h3>Notas</h3>
            <br />
            <ul>
              <li>Termina con <code>;</code>.</li>
              <br />
              <li>La instrucción <code>return</code> se usa para devolver el resultado.</li>
              <br />
              <li>El tipo de retorno debe declararse después del operador <code>=&gt;</code>.</li>
              <br />
              <li>Las funciones pueden ser llamadas desde cualquier parte del programa después de ser definidas.</li>
            </ul>
          </section>
        )}

        {section === "currificables" && (
          <section>
            <h2>Funciones Currificables</h2>

            <p>
              En <strong>KAFE</strong>, las funciones currificables son funciones que pueden invocarse parcialmente. Este
              enfoque proviene del paradigma funcional, y permite que una función que recibe múltiples parámetros pueda ser
              ejecutada parcialmente con uno o más argumentos, devolviendo una nueva función que espera los restantes.
            </p>

            <p>
              Esta característica es especialmente útil cuando quieres reutilizar una función con ciertos parámetros ya
              definidos, creando funciones más especializadas a partir de otras más generales.
            </p>

            <h3>Sintaxis Básica</h3>

            <pre><code>{
        `drip nombreFuncion(param1: TIPO1, param2: TIPO2) => TIPO_RETORNO:
            // cuerpo
        ;`
        }</code></pre>

            <p>
              La palabra clave <code>drip</code> indica que la función puede currificarse. Puedes invocar la función pasando
              todos los argumentos de una vez o parcialmente, dejando que se genere una nueva función intermedia.
            </p>

            <h3>Ejemplo</h3>

            <p>A continuación se define una función <code>sumar</code> que suma dos enteros:</p>

            <pre><code>{
        `drip sumar(a: INT, b: INT) => VOID:
            show(a + b);
        ;`
        }</code></pre>

            <p>Puedes invocarla de las siguientes formas:</p>

            <pre><code>{
        `sumar(10)(5);   // Currificación — devuelve 15
        sumar(10, 5);   // Llamada directa — también devuelve 15`
        }</code></pre>

            <p>
              La primera llamada es una aplicación parcial: al ejecutar <code>sumar(10)</code> se genera una función
              intermedia que espera un segundo parámetro. Luego, <code>(5)</code> se aplica a esa función.
            </p>

            <h3>Asignación como Función de Orden Superior</h3>

            <p>
              Puedes guardar una función ya parcialmente aplicada en una variable, para luego reutilizarla múltiples veces con
              diferentes argumentos:
            </p>

            <pre><code>{
        `FUNC(INT)=>INT sumarQuince = sumar(15);`
        }</code></pre>

            <p>
              En este caso, <code>sumarQuince</code> es una función que espera un <code>INT</code> y devuelve un
              <code>INT</code>. Internamente, es equivalente a <code>sumar(15)(x)</code> para cualquier valor <code>x</code>.
            </p>

            <p>Luego puedes hacer:</p>

            <pre><code>{
        `sumarQuince(5);    // Imprime 20
        sumarQuince(100);  // Imprime 115`
        }</code></pre>

            <h3>Ventajas</h3>

            <ul>
              <li>
                <strong>Reutilización de lógica:</strong> permite definir funciones base y luego especializarlas con valores
                parciales.
              </li>
              <li>
                <strong>Modularidad:</strong> promueve un estilo de programación más declarativo y composicional.
              </li>
              <li>
                <strong>Expresividad:</strong> permite escribir código más claro y directo en contextos funcionales.
              </li>
            </ul>

            <p>
              Las funciones currificables en KAFE combinan claridad sintáctica con poder expresivo, facilitando la creación de
              código reusable y elegante.
            </p>

          </section>
        )}
        {section === "alto-nivel" && (
            <section>
            <h2>Funciones de Alto Nivel</h2>

            <p>
              En <strong>KAFE</strong>, las funciones de alto nivel (también llamadas funciones de orden superior) son aquellas
              que aceptan otras funciones como parámetros o que retornan funciones. Este tipo de programación proviene del
              paradigma funcional y es fundamental para la composición, reutilización de lógica y abstracción de patrones.
            </p>

            <h3>Sintaxis Básica</h3>

            <p>La estructura general de una función de alto nivel en KAFE es:</p>

            <pre><code>{
        `drip nombreFuncion(f: FUNC(TIPO_IN) => TIPO_OUT, otro_param: TIPO) => TIPO_RETORNO:
            // cuerpo
        ;`
        }</code></pre>

            <p>
              Aquí, <code>f</code> es una función que puede ser pasada como argumento. El tipo <code>FUNC(...)</code> declara
              el tipo de entrada y salida de esa función.
            </p>

            <h3>Ejemplo con Función Nombrada</h3>

            <p>Veamos un ejemplo con una función llamada <code>inc</code> que incrementa un valor entero:</p>

            <pre><code>{
        `drip aplicar(f: FUNC(INT) => INT, n: INT) => INT:
            return f(n);
        ;

        drip inc(x: INT) => INT:
            return x + 1;
        ;

        show(aplicar(inc, 5));   // 6`
        }</code></pre>

            <p>
              En este ejemplo, la función <code>aplicar</code> recibe otra función <code>f</code> y un valor <code>n</code>, y
              retorna el resultado de aplicar <code>f(n)</code>. Como estamos pasando <code>inc</code>, se incrementa el valor
              5.
            </p>

            <h3>Ejemplo con Lambda</h3>

            <p>
              También puedes pasar funciones anónimas (lambdas) directamente como argumento, sin necesidad de definirlas antes:
            </p>

            <pre><code>{
        `show(aplicar((y: INT) => y*y , 4));   // 16`
        }</code></pre>

            <p>
              Aquí, la función lambda  se pasa directamente a <code>aplicar</code>, elevando al
              cuadrado el número 4.
            </p>

            <h3>Ventajas</h3>

            <ul>
              <li>
                <strong>Abstracción:</strong> puedes encapsular patrones de ejecución y lógica genérica sin repetir código.
              </li>
              <li>
                <strong>Reutilización:</strong> permite separar la lógica del comportamiento, pasando distintas funciones según
                el contexto.
              </li>
              <li>
                <strong>Composición funcional:</strong> facilita trabajar con funciones que se combinan o modifican.
              </li>
            </ul>

            <p>
              Las funciones de alto nivel son fundamentales para escribir código más flexible, expresivo y modular. Su uso se
              potencia aún más al combinarse con <strong>funciones currificables</strong> y <strong>lambdas</strong>, como se
              muestra en los ejemplos anteriores.
            </p>
          </section>
        )}
        {section === "recursivas" && (
          <section>
            <h2>Función Recursiva: Factorial</h2>

    <p>
      En <strong>KAFE</strong>, es posible definir funciones <strong>recursivas</strong>, es decir, funciones que se llaman a sí mismas.
      Un ejemplo clásico de recursividad es el cálculo del factorial de un número.
    </p>

    <h3>¿Qué es el factorial?</h3>
    <p>
      El factorial de un número entero positivo <code>n</code> (denotado como <code>n!</code>) se define como:
    </p>

    <pre><code>{
`n! = n * (n - 1) * (n - 2) * ... * 1`
}</code></pre>

    <p>
      Por ejemplo: <code>5! = 5 * 4 * 3 * 2 * 1 = 120</code>
    </p>

    <h3>Sintaxis de la Función en KAFE</h3>

    <pre><code>{
`drip factorial(n: INT) => INT:
    if (n <= 1):
        return 1;
    ;
    return n * factorial(n - 1);
;`
}</code></pre>

    <p>
      La función <code>factorial</code> recibe un entero <code>n</code>. Si <code>n</code> es menor o igual a 1, retorna 1 (caso base).
      En caso contrario, se llama a sí misma con <code>n - 1</code>, construyendo la multiplicación de forma descendente.
    </p>

    <h3>Ejemplo de Uso</h3>

    <pre><code>{
`INT result = factorial(5);
show("Factorial de 5:");
show(result);`
}</code></pre>

    <p>
      Este código muestra el resultado del cálculo de <code>factorial(5)</code>, que es <strong>120</strong>.
    </p>

    <h3>¿Cómo funciona paso a paso?</h3>

    <ul>
      <li><code>factorial(5)</code> → 5 × factorial(4)</li>
      <li><code>factorial(4)</code> → 4 × factorial(3)</li>
      <li><code>factorial(3)</code> → 3 × factorial(2)</li>
      <li><code>factorial(2)</code> → 2 × factorial(1)</li>
      <li><code>factorial(1)</code> → 1 (caso base)</li>
    </ul>

    <p>
      Al ir resolviendo cada llamada recursiva, el resultado final se calcula como <code>5 * 4 * 3 * 2 * 1 = 120</code>.
    </p>

    <h3>Ventajas</h3>

    <ul>
      <li>Permite escribir soluciones elegantes para problemas que siguen un patrón repetitivo.</li>
      <li>Evita el uso de bucles explícitos.</li>
      <li>Ayuda a pensar de forma declarativa: qué hacer, no cómo hacerlo paso a paso.</li>
    </ul>

    <p>
      Aunque la recursión es poderosa, hay que usarla con cuidado para evitar llamadas infinitas y errores de pila.
      Siempre asegúrate de tener un <strong>caso base bien definido</strong>.
    </p>
          </section>
        )}
      </main>
    </div>
  );
}
