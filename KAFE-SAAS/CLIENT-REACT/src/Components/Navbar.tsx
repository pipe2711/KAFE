import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

import logoDark from '../assets/1.png';
import logoLight from '../assets/2.png';

export const Navbar = () => {
  const [isLight, setIsLight] = useState(false);

  useEffect(() => {
    const observer = new MutationObserver(() => {
      setIsLight(document.body.classList.contains('light-theme'));
    });

    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ['class'],
    });

    // estado inicial
    setIsLight(document.body.classList.contains('light-theme'));

    return () => observer.disconnect();
  }, []);

  const logo = isLight ? logoDark : logoLight;

  return (
    <header className="navbar">
      <div className="logo">
        <Link to="/">
          <img src={logo} alt="KAFE logo" />
        </Link>
      </div>
      <nav className="nav-links">
        <Link to="/">Inicio</Link>
        <Link to="/editor">Editor</Link>
        <Link to="/docs">Documentación</Link>
        <Link to="/login">Login</Link>
      </nav>
    </header>
  );
};
