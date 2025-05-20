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
                <a href="#install">Installation</a>
              </li>
              <li>
                <a href="#quick">Quick Start Guide</a>
              </li>
              <li>
                <a href="#structure">Project Structure</a>
              </li>
            </ul>
          </details>
          <details>
            <summary>Components</summary>
            <ul>
              <li>Stepper</li>
              <li>Tabs</li>
              <li>Note</li>
              <li>Code Block</li>
              <li>Image & Link</li>
              <li>
                File System <span className="badge">New</span>
              </li>
              <li>Custom</li>
            </ul>
          </details>
          <ul>
            <li>Internationalization</li>
            <li>
              Algolia Search <span className="badge">New</span>
            </li>
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
          Inicialmente, <strong>KAFE</strong> está pensado para ejecutarse en este entorno web: puedes escribir tu código, compilarlo, 
          descargar los archivos generados y, si deseas continuar más adelante, simplemente vuelve a subirlos para 
          seguir trabajando donde lo dejaste.
        </p>
      </section>

        <section id="install">
          <h2>Installation</h2>
          <p>
            Puedes instalar el intérprete de KAFE desde nuestra página oficial o
            usar un contenedor Docker preconfigurado.
          </p>
        </section>

        <section id="quick">
          <h2>Quick Start Guide</h2>
          <p>
            Sigue esta guía rápida para comenzar a definir tu primer modelo en
            KAFE.
          </p>
          <pre>{`CODIGUITO`}</pre>
        </section>

        <section id="structure">
          <h2>Project Structure</h2>
          <p>Organiza tu proyecto KAFE de la siguiente manera:</p>
          <pre>{`src/
 ├── models/
 ├── datasets/
 ├── run.kf`}</pre>
        </section>
      </main>
    </div>
  );
}
