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
          <h1>Introduction</h1>
          <p>
            KAFE es un lenguaje diseñado para facilitar la definición de redes
            neuronales en contextos educativos.
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
