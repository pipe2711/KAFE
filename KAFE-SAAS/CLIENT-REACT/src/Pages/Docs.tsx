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
            <ul>
              <li><a onClick={() => setSection("numk")}>Numk</a></li>
            </ul>
          </details> 
          <details open>
            <summary>Plot<span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("plot")}>Plot</a></li>
            </ul>
          </details> 
          <details open>
            <summary>Math <span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("math")}>Math</a></li>
            </ul>
          </details> 
          <details open>
            <summary>Files <span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("files")}>Files</a></li>
            </ul>
          </details> 
          <details open>
            <summary>GeshaDeep<span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("gesha")}>GeshaDeep</a></li>             
            </ul>
          </details>
          <details open>
            <summary>Pardos<span className="badge">New</span></summary>
            <ul>
              <li><a onClick={() => setSection("pardos")}>Pardos</a></li>
            </ul>
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
        {section === "numk" && (
          <section>
            <h2>Numk</h2>
            <p>
              Numk es nuestra librería de cálculo numérico en KAFE. Proporciona funciones para trabajar con álgebra escalar,
              vectores y matrices (suma, multiplicación, transposición e inversa), de forma sencilla e intuitiva.
            </p>

            <h3>Importar Numk</h3>
            <p>
            </p>
            <pre><code>{`import numk;`}</code></pre>
            <p>

            </p>

            <h3>Operaciones con matrices</h3>
            <p>

            </p>

            <h4>1. Suma de dos matrices</h4>
            <pre><code>{`--Prueba Sumar Matrices
        import numk;

        List[List[INT]] A = [[1, 2], [3, 4]];
        List[List[INT]] B = [[5, 6], [7, 8]];

        List[List[INT]] C = numk.add(A, B);
        show(C);  --[[6,8],[10,12]]`}</code></pre>
            <p>

            </p>

            <h4>2. Multiplicación de matrices</h4>
            <pre><code>{`--Prueba Multiplicar Matrices
        import numk;

        List[List[INT]] A = [[1, 2]];
        List[List[INT]] B = [[2], [3]];

        List[List[INT]] C = numk.mul(A, B);
        show(C);  --[[8]]`}</code></pre>
            <p>

            </p>

            <h4>3. Transposición</h4>
            <pre><code>{`--Prueba Transpuesta
        import numk;

        List[List[INT]] A = [
          [1, 2],
          [3, 4],
          [5, 6]
        ];

        show(numk.transpose(A));  --[[1,3,5],[2,4,6]]`}</code></pre>
            <p>

            </p>

            <h4>4. Inversa de una matriz</h4>
            <pre><code>{`-- Prueba Inversa
        import numk;

        List[List[INT]] A = [
          [2, 1],
          [7, 4]
        ];

        show(numk.inv(A));
        --[[4.0, -1.0], [-7.0, 2.0]]`}</code></pre>
            <p>

            </p>

            <h3>Notas</h3>
            <ul>
              <li><strong>Tipos soportados:</strong> <code>INT</code> y <code>FLOAT</code>.</li><br/>
              <li>
                <strong>Dimensiones compatibles:</strong>
                <ul>
                  <li>Para <code>add</code> y <code>mul</code>, las matrices deben tener dimensiones compatibles
                      (suma: mismo tamaño; multiplicación: cols A = rows B).</li>
                  <li>Para <code>inv</code>, la matriz debe ser cuadrada e invertible.</li>
                  <li><code>transpose</code> acepta cualquier matriz filas×columnas.</li>
                </ul>
              </li><br/>
              <li>Si las dimensiones no encajan, Numk lanzará un error de dimensión.</li>
            </ul>
          </section>
        )}
        {section === "plot" && (
          <section>
            <h2>Plot</h2>
            <p>
              Plot es la librería de visualización de KAFE. Permite crear gráficas de barras,
              líneas y pastel, así como configurar títulos, etiquetas, colores y leyendas
              de forma muy sencilla.
            </p>

            <h3>Importar Plot</h3>
            <pre><code>{`import plot;`}</code></pre>
            <p>

            </p>
            <h3>Inicializar figura</h3>
            <pre><code>{`plot.figure();`}</code></pre>
            <p>
              
            </p>

            <h3>Títulos y etiquetas</h3>
            <pre><code>{`plot.title("Mi Gráfica");
        plot.xlabel("Eje X");
        plot.ylabel("Eje Y");`}</code></pre>
            <p>
              
            </p>

            <h3>Rejilla</h3>
            <pre><code>{`plot.grid(true);`}</code></pre>
            <p>
              
            </p>

            <h3>Colores</h3>
            <pre><code>{`plot.color("blue");
        plot.pointColor("orange");`}</code></pre>
            <p>
              
            </p>

            <h3>Gráfica de líneas (simple)</h3>
            <pre><code>{`List[INT] t = [0, 1, 2, 3, 4];
        List[INT] h = [0, 10, 40, 90, 160];

        plot.graph(t, h);
        plot.render();`}</code></pre>
            <p>
              
            </p>

            <h3>Gráfica de barras</h3>
            <pre><code>{`List[STR] libs = ["Matplotlib", "Seaborn", "Plotly", "Plotnine"];
        List[INT] users = [2500, 1800, 3000, 2200];

        plot.bar(libs, users);
        plot.title("Bibliotecas más populares");
        plot.ylabel("Usuarios");
        plot.render();`}</code></pre>
            <p>
              
            </p>

            <h3>Gráfica de pastel</h3>
            <pre><code>{`List[STR] frutas = ["Manzanas", "Peras", "Bananas", "Uvas"];
        List[INT] cantidades = [25, 15, 35, 25];

        plot.pie(frutas, cantidades);
        plot.legend("Distribución de frutas");
        plot.render();`}</code></pre>
            <p>
              
            </p>

            <h3>Múltiples series en la misma gráfica</h3>
            <p>
              
            </p>
            <p>
              Para superponer varias curvas o conjuntos de puntos, basta con llamar varias veces
              al método deseado (<code>graph</code> o <code>bar</code>) antes de <code>render()</code>:
            </p>
            <pre><code>{`List[INT] x = [0, 1, 2, 3, 4];
        List[INT] y1 = [0,  5, 10, 15, 20];
        List[INT] y2 = [10, 8,  6,  4,  2];

        plot.figure();
        plot.color("red");
        plot.graph(x, y1);       -- Primera serie en rojo
        plot.color("green");
        plot.graph(x, y2);       -- Segunda serie en verde
        plot.title("Dos series de ejemplo");
        plot.xlabel("X");
        plot.ylabel("Y");
        plot.legend("Serie A");
        plot.legend("Serie B");
        plot.render();`}</code></pre>
            <p>
              
            </p>

            <h3>Notas</h3>
            <p>
              
            </p>
            <ul>
              <li>Llama a <code>plot.figure()</code> al inicio de cada visualización.</li><br/>
              <li>Configura siempre <code>title</code>, <code>xlabel</code> y <code>ylabel</code>.</li><br/>
              <li>Usa <code>grid(true)</code> para mejorar la legibilidad.</li><br/>
              <li>Define colores antes de cada llamada si quieres distinguir series.</li><br/>
              <li>Para múltiples series, llama varias veces a <code>graph</code>.</li><br/>
            </ul>
          </section>
        )}
        {section === "math" && (
          <section>
            <h2>Math</h2>
            <p>

            </p>
            <p>
              Math es la librería de utilidades matemáticas de KAFE. Incluye constantes,
              funciones trigonométricas, exponenciales, logaritmos, combinatoria,
              operaciones sobre enteros, manipulación de coma flotante, funciones especiales
              y más.
            </p>
            <p>
              
            </p>

            <h3>Importar Math</h3>
            <pre><code>{`import math;`}</code></pre>
            <p>
              
            </p>

            <h3>Ejemplo completo</h3>
            <pre><code>{`import math;

        -- Constantes
        show(math.pi);
        show(math.e);
        show(math.tau);
        show(math.inf);
        show(math.nan);

        -- Trigonometría
        show(math.sin(math.pi/2));
        show(math.cos(0));
        show(math.tan(math.pi/4));

        -- Inversas
        show(math.asin(1));
        show(math.acos(1));
        show(math.atan(1));

        -- Hiperbólicas
        show(math.sinh(0));
        show(math.cosh(0));
        show(math.tanh(0));

        -- Exponenciales y logaritmos
        show(math.exp(1));
        show(math.expm1(1));
        show(math.log(math.e));
        show(math.log(8, 2));
        show(math.log2(8));
        show(math.log10(1000));
        show(math.exp2(3));
        show(math.cbrt(27));

        -- Potencia y raíz
        show(math.sqrt(16));
        show(math.pow(2, 8));

        -- Funciones número-teóricas
        show(math.factorial(5));
        show(math.comb(5, 2));
        show(math.perm(5, 2));
        show(math.gcd(48, 18));
        show(math.gcd(48, 18, 30));
        show(math.lcm(12, 15));
        show(math.lcm(12, 15, 20));

        -- Aritmética de coma flotante
        show(math.abs(-42));
        show(math.trunc(3.7));
        show(math.trunc(-3.7));
        show(math.fmod(7.3, 2.5));
        show(math.fmod(-7.3, 2.5));
        show(math.remainder(7.3, 2.5));
        show(math.remainder(-7.3, 2.5));
        show(math.copysign(3, -0.0));
        show(math.copysign(-3, 5));
        show(math.isclose(1.0000000000001, 1));
        show(math.isfinite(math.inf));
        show(math.isinf(math.inf));
        show(math.isnan(math.nan));
        show(math.ulp(1.0));
        show(math.ulp(0.0));

        -- Sumatorio y producto
        show(math.sum(1, 5));
        show(math.sum(range(6)));
        show(math.prod(1, 5));
        show(math.sumprod([1,2,3], [4,5,6]));

        -- Distancia y fsum/hypot
        show(math.dist([0,0], [3,4]));
        show(math.fsum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]));
        show(math.hypot(3, 4));`}</code></pre>
            <p>
              
            </p>

            <h3>Descripción de funciones</h3><br/>
            <ul>
              <li><strong>Constantes:</strong> <code>pi, e, tau, inf, nan</code>.</li><br/>
              <li><strong>Trigonométricas e inversas:</strong> <code>sin, cos, tan, asin, acos, atan</code> (argumentos en radianes).</li><br/>
              <li><strong>Hiperbólicas:</strong> <code>sinh, cosh, tanh</code>.</li><br/>
              <li><strong>Exponenciales/logaritmos:</strong> <code>exp, expm1, log(x[,base]), log2, log10, exp2, cbrt</code>.</li><br/>
              <li><strong>Potencia y raíz:</strong> <code>pow, sqrt</code>.</li><br/>
              <li><strong>Combinatoria:</strong> <code>factorial, comb(n,k), perm(n,k)</code>.</li><br/>
              <li><strong>Número-teóricas:</strong> <code>gcd(...), lcm(...)</code>.</li><br/>
              <li><strong>Flotantes:</strong> <code>abs, trunc, fmod, remainder, copysign, isclose, isfinite, isinf, isnan, ulp</code>.</li><br/>
              <li><strong>Sumatorio/producto:</strong> <code>sum(a,b), sum(list), prod(a,b), prod(list), sumprod(list1,list2)</code>.</li><br/>
              <li><strong>Distancia y precisión:</strong> <code>dist, fsum, hypot</code>.</li><br/>
            </ul>

            <h3>Notas</h3><br/>
            <ul>
              <li>Argumentos de trigonometría en radianes.</li><br/>
              <li><code>log</code> acepta base opcional como segundo parámetro.</li><br/>
              <li>Funciones número-teóricas requieren enteros.</li><br/>
              <li><code>isnan</code> y <code>isinf</code> ayudan a detectar valores especiales.</li><br/>
              <li><code>fsum</code> y <code>hypot</code> ofrecen mayor precisión en flotantes.</li><br/>
            </ul>
          </section>
        )}
        {section === "files" && (
          <section>
            <h2>Files</h2>
            <p>

            </p>
            <p>
              Files es la librería de manejo de archivos de KAFE. Permite crear, escribir,
              leer, anexar y eliminar archivos de texto de manera sencilla.
            </p>
            <p>
              
            </p>

            <h3>Importar Files</h3>
            <pre><code>{`import files;`}</code></pre>
            <p>
              
            </p>

            <h3>Crear un archivo</h3>
            <pre><code>{`-- Crea un archivo vacío (si ya existe, no hace nada)
        files.create("mi_archivo.txt");`}</code></pre>
            <p>
              
            </p>

            <h3>Escribir en un archivo</h3>
            <pre><code>{`-- Escribe (o sobreescribe) contenido en el archivo
        files.write("mi_archivo.txt", "Hola desde KAFE");`}</code></pre>
            <p>
              
            </p>

            <h3>Leer un archivo</h3>
            <pre><code>{`-- Lee todo el contenido como STR
        STR texto = files.read("mi_archivo.txt");
        show(texto);`}</code></pre>
            <p>
              
            </p>

            <h3>Anexar al archivo</h3>
            <pre><code>{`-- Agrega contenido al final del archivo
        files.append("mi_archivo.txt", "\nMás texto en la siguiente línea");`}</code></pre>
            <p>
              
            </p>

            <h3>Eliminar un archivo</h3>
            <pre><code>{`-- Borra el archivo
        files.delete("mi_archivo.txt");`}</code></pre>
            <p>
              
            </p>

            <h3>Ejemplo completo</h3>
            <pre><code>{`import files;

        -- Crear y escribir
        files.create("notas.txt");
        files.write("notas.txt", "Primera línea");

        -- Anexar más contenido
        files.append("notas.txt", "\nSegunda línea");

        -- Leer y mostrar
        STR contenido = files.read("notas.txt");
        show(contenido);  -- "Primera línea\nSegunda línea"

        -- Eliminar cuando ya no se necesite
        files.delete("notas.txt");`}</code></pre>
            <p>
              
            </p>

            <h3>Notas y buenas prácticas</h3>
            <ul><br/>
              <li>
                <strong>Rutas relativas:</strong> todos los archivos se crean en el directorio de trabajo.
              </li><br/>
              <li>
                <strong>files.write</strong> sobrescribe el contenido existente; usa <code>append</code> para no perder datos.
              </li><br/>
              <li>
                <strong>files.read</strong> devuelve todo como <code>STR</code>; si el archivo no existe, lanza un error.
              </li><br/>
            </ul>
          </section>
        )}

{section === "gesha" && (
  <section>
    <h2>GeshaDeep</h2><br/>
    <p>
      GeshaDeep es la librería de machine learning de KAFE. Soporta modelos
      de clasificación binaria, multiclase, regresión lineal y clustering, con
      una API unificada basada en “modelos” y “capas”.
    </p><br/>

    <h3>Importar GeshaDeep</h3>
    <pre><code>{`import geshaDeep;`}</code></pre><br/>

    <h3>1. Clasificación AND (binaria)</h3><br/>
    <p>
      Este ejemplo entrena una red de una sola neurona con activación sigmoid 
      para resolver la función lógica AND. Tras el entrenamiento, predice la 
      probabilidad y la etiqueta (0 o 1) para cada combinación de entrada.
    </p>
    <pre><code>{`-- Dataset AND
List[List[INT]] x_train = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
];
List[INT] y_train = [0, 0, 0, 1];

GESHA model = geshaDeep.binary();
GESHA layer = geshaDeep.create_dense(1, "sigmoid", [2], 0.0, 42);
model.add(layer);

model.compile("sgd", "binary_crossentropy", ["accuracy"]);
model.fit(x_train, y_train, 1000, 1, [], []);

-- Probamos los 4 puntos
for (p in x_train):
    FLOAT prob = model.predict_proba(p);  -- probabilidad clase 1
    INT   lbl  = model.predict_label(p);  -- etiqueta 0/1
    show(str(p) + " -> prob=" + str(prob) + ", label=" + str(lbl));
;`}</code></pre><br/>

    <h3>2. Clasificación OR (multiclase)</h3><br/>
    <p>
      Aquí usamos una red con capa oculta ReLU y capa de salida softmax
      para la función OR, codificada one-hot. Se incluye también un pequeño
      conjunto de validación y al final obtenemos las probabilidades para un
      nuevo ejemplo y el resumen del modelo.
    </p>
    <pre><code>{`-- classification_predict.kf
import geshaDeep;

-- OR lógico:  class0=[1,0], class1=[0,1]
List[List[INT]] x_train = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
];
List[List[INT]] y_train = [
    [1,0],
    [0,1],
    [0,1],
    [0,1]
];

-- pequeña validación
List[List[INT]] x_val = [[0,0],[1,1]];
List[List[INT]] y_val = [[1,0],[0,1]];

GESHA model = geshaDeep.categorical();
GESHA h  = geshaDeep.create_dense(4, "relu",  [2], 0.0, 42);
GESHA out = geshaDeep.create_dense(2, "softmax", [4], 0.0, 42);
model.add(h);
model.add(out);

model.compile("sgd", "categorical_crossentropy", ["accuracy"]);
model.fit(x_train, y_train, 100, 2, x_val, y_val);

-- predicción para [1,0]  (esperamos class1)
List[INT] sample = [1,0];
List[FLOAT] probs = model.predict(sample);
show("Probabilidades: " + str(probs));

model.summary();`}</code></pre><br/>

    <h3>3. Regresión Lineal</h3><br/>
    <p>
      Este ejemplo ajusta una regresión lineal simple con una única neurona
      de activación lineal. Tras entrenar con MSE, predice un nuevo valor y
      usa Plot para mostrar la línea de regresión junto a los puntos de 
      entrenamiento y validación.
    </p>
    <pre><code>{`import geshaDeep;
import plot;

List[List[INT]] x_train = [[0], [1], [2], [3], [4]];
List[FLOAT]     y_train = [1.0,  4.0,  7.0, 10.0, 13.0];

List[List[INT]] x_val   = [[6]];
List[FLOAT]     y_val   = [19.0];

GESHA model = geshaDeep.regression();

GESHA dense = geshaDeep.create_dense(1, "linear", [1], 0.0, 42);
model.add(dense);

geshaDeep.compile(model, "sgd", "mse", []);

model.fit(x_train, y_train, 200, 1, x_val, y_val);

List[INT] sample = [6];
FLOAT y_pred = model.predict(sample)[0];
show("Predicción para 6: " + str(y_pred));

model.summary();

List[List[FLOAT]] train_points = [];
for (i in range(0, len(x_train))):
    FLOAT xi = float(x_train[i][0]);
    FLOAT yi = y_train[i];
    append(train_points, [xi, yi]);
;

List[List[FLOAT]] val_points = [];
for (i in range(0, len(x_val))):
    FLOAT xv = float(x_val[i][0]);
    FLOAT yv = y_val[i];
    append(val_points, [xv, yv]);
;

List[List[FLOAT]] line_points = [];
for (i in range(0, 7)):
    List[INT] xi_int = [i];
    FLOAT yi_pred = model.predict(xi_int)[0];
    append(line_points, [float(i), yi_pred]);
;

plot.figure();
plot.title("Regresión lineal con GeshaDeep: y = 3x + 1");
plot.xlabel("X");
plot.ylabel("Y");
plot.grid(True);

if (len(line_points) > 0):
    plot.pointColor("blue");
    plot.pointSize(2);
    plot.graph(line_points, "line");
;

if (len(train_points) > 0):
    plot.pointColor("red");
    plot.pointSize(8);
    plot.graph(train_points, "point");
;

if (len(val_points) > 0):
    plot.pointColor("green");
    plot.pointSize(12);
    plot.graph(val_points, "point");
;

plot.legend("línea de regresión (azul) ; train (rojo) ; val (verde)");
plot.render();`}</code></pre><br/>

    <h3>4. Clustering</h3><br/>
    <p>
      El modelo de clustering utiliza la función k-means. Tras añadir dos capas
      densas y compilar con “adam”, el modelo ajusta los datos sin etiquetas.
      Luego, asigna cada punto a un clúster, calcula sus centroides y visualiza
      resultados con Plot.
    </p>
    <pre><code>{`import geshaDeep;
import plot;


List[List[FLOAT]] datos = [
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0]
];

List[INT] y_dummy = [];


GESHA modelo = geshaDeep.clustering();


GESHA capa1 = geshaDeep.create_dense(
    8,         -- 4 neuronas en primera capa oculta
    "relu",    
    [2],       -- entrada 2D
    0.0,       
    12         -- semilla distinta
);
modelo.add(capa1);


GESHA capa1b = geshaDeep.create_dense(
    4,        
    "relu",   
    [],       
    0.0,
    99        
);
modelo.add(capa1b);


GESHA capa2 = geshaDeep.create_dense(
    2, "softmax", [], 0.0, 42
);
modelo.add(capa2);


geshaDeep.compile(modelo, "adam", "categorical_crossentropy", []);

geshaDeep.set_lr(modelo, 0.0005);


modelo.fit(datos, y_dummy, 300, 2);


List[FLOAT] X0 = [];
List[FLOAT] Y0 = [];
List[FLOAT] X1 = [];
List[FLOAT] Y1 = [];

List[INT] indices = [0,1,2,3,4,5];
for (i in indices):
    List[FLOAT] punto = datos[i];
    List[FLOAT] probs = modelo.predict(punto);
    show(probs);  -- imprimo probabilidades para ver evolución
    
    FLOAT p0 = probs[0];
    FLOAT p1 = probs[1];
    INT etiqueta;
    if (p0 >= p1):
        etiqueta = 0;
    else:
        etiqueta = 1;
    ;
    
    FLOAT xi = punto[0];
    FLOAT yi = punto[1];
    if (etiqueta == 0):
        append(X0, xi);
        append(Y0, yi);
    else:
        append(X1, xi);
        append(Y1, yi);
    ;
;


FLOAT sumx0 = 0.0; FLOAT sumy0 = 0.0; INT count0 = 0;
FLOAT sumx1 = 0.0; FLOAT sumy1 = 0.0; INT count1 = 0;

for (i in indices):
    List[FLOAT] punto = datos[i];
    List[FLOAT] probs = modelo.predict(punto);
    FLOAT p0 = probs[0];
    FLOAT p1 = probs[1];
    INT etiqueta;
    if (p0 >= p1):
        etiqueta = 0;
    else:
        etiqueta = 1;
    ;
    FLOAT xi = punto[0];
    FLOAT yi = punto[1];
    if (etiqueta == 0):
        sumx0 = sumx0 + xi;
        sumy0 = sumy0 + yi;
        count0 = count0 + 1;
    else:
        sumx1 = sumx1 + xi;
        sumy1 = sumy1 + yi;
        count1 = count1 + 1;
    ;
;

FLOAT cx0;
if (count0 == 0):
    cx0 = 0.0;
else:
    cx0 = sumx0 / count0;
;

FLOAT cy0;
if (count0 == 0):
    cy0 = 0.0;
else:
    cy0 = sumy0 / count0;
;

FLOAT cx1;
if (count1 == 0):
    cx1 = 0.0;
else:
    cx1 = sumx1 / count1;
;

FLOAT cy1;
if (count1 == 0):
    cy1 = 0.0;
else:
    cy1 = sumy1 / count1;
;

List[FLOAT] CX = [cx0, cx1];
List[FLOAT] CY = [cy0, cy1];


List[List[FLOAT]] pares0 = [];
for (i in range(0, len(X0))):
    append(pares0, [X0[i], Y0[i]]);
;

List[List[FLOAT]] pares1 = [];
for (i in range(0, len(X1))):
    append(pares1, [X1[i], Y1[i]]);
;

List[List[FLOAT]] centros = [];
for (i in range(0, len(CX))):
    append(centros, [CX[i], CY[i]]);
;


plot.figure();
plot.title("Clustering k-means (k=2) ― GeshaDeep (2 capas de 4 → 4, lr=0.0005)");
plot.xlabel("X");
plot.ylabel("Y");
plot.grid(True);


if (len(pares0) > 0):
    plot.pointColor("red");
    plot.pointSize(6);
    plot.graph(pares0, "point");
;

if (len(pares1) > 0):
    plot.pointColor("green");
    plot.pointSize(6);
    plot.graph(pares1, "point");
;

if (len(centros) > 0):
    plot.pointColor("black");
    plot.pointSize(8);
    plot.graph(centros, "point");
;

plot.legend("red: clúster 0 ; green: clúster 1 ; black: centros");
plot.render();`}</code></pre><br/>

    <h3>Notas y buenas prácticas</h3><br/>
    <ul>
      <li>
        Para clasificación usa <code>binary()</code> (sigmoid) o <code>categorical()</code> (softmax).
      </li><br/>
      <li>
        En regresión lineal, utiliza <code>regression()</code> y capa “linear” con pérdida MSE.
      </li><br/>
      <li>
        Añade capas con <code>create_dense</code> antes de <code>compile</code> y <code>fit</code>.
      </li><br/>
      <li>
        Usa Plot para visualizar aprendizaje y resultados de forma rápida.
      </li>
    </ul>
  </section>
)}

        {section === "pardos" && (
          <section>
            <p>
          PROXIMAMENTE...
            </p> 
          </section>
        )}
      </main>
    </div>
  );
}
