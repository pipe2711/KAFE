import { Link } from 'react-router-dom';
import { Button } from '../Components/Button';

export default function Home() {
  return (
    <section className="section">
      <h1 className="title">KAFE</h1>
      <p className="subtitle">Deep Learning Language para todos</p>
      <div className="actions">
        <Link to="/editor">
          <Button>Comenzar Ahora</Button>
        </Link>
        <Link to="/docs">
          <Button variant="dark">Ver Documentación</Button>
        </Link>
      </div>
    </section>
  );
}
