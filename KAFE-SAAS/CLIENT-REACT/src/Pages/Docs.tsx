export default function Docs() {
  return (
    <div className="docs-layout">
      <aside className="docs-sidebar">
        <h2 className="sidebar-title">KAFE Docs</h2>
        <nav className="sidebar-nav">
          <details open>
            <summary>Getting Started</summary>
            <ul>
              <li>
                <a href="#intro">Introduction</a>
              </li>
              <li>
                <a href="#quick">Quick Start Guide</a>
              </li>
            </ul>
          </details>
          <details open>
          <summary>Lenguaje KAFE<span className="badge">New</span></summary>
          <ul>
            <li><a href="#comentarios">Comentarios</a></li>
            <li><a href="#variables">Variables y Tipos</a></li>
            <li><a href="#numeros-strings">Números y Strings</a></li>
            <li><a href="#booleanos-operadores">Booleanos y Operadores</a></li>
            <li><a href="#listas-matrices">Listas y Matrices</a></li>
            <li><a href="#condicionales">Condicionales</a></li>
            <li><a href="#bucles">Bucles</a></li>
            <li><a href="#funciones">Funciones</a></li>
            <li><a href="#currificables">Funciones Currificables</a></li>
            <li><a href="#alto-nivel">Funciones de Alto Nivel</a></li>
            <li><a href="#recursivas">Funciones Recursivas</a></li>
          </ul>
        </details>

          <ul>
          <details open>
            <summary>NUMK<span className="badge">New</span></summary>
            </details>
            <details open>
            <summary>KAFEPLOT<span className="badge">New</span></summary>
            </details>
            <details open>
            <summary>KAFEMATH<span className="badge">New</span></summary>
            </details>
            <details open>
            <summary>GESHADEEP<span className="badge">New</span></summary>
            </details>
            <li>Themes</li>
            <li>Customize</li>
          </ul>
        </nav>
      </aside>

      <main className="docs-content">
      <section id="intro">
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
        <section id="quick">
  <h2>Quick Start Guide</h2>
  <p>
    Para comenzar rápidamente, abre el <strong>Editor</strong> en línea desde el menú principal y pega el siguiente código. 
    Puedes ejecutarlo inmediatamente para ver el resultado.
  </p>
  <p>
    Este ejemplo importa el módulo <code>NUMK</code> y realiza una operación aritmética básica.
  </p>
  <pre>{`import NUMK;

let a = 5;
let b = 10;
let resultado = a + b;
show(resultado);`}</pre>
</section>


      </main>
    </div>
  );
}
