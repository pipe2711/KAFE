import { useEffect, useState } from 'react';

export const ThemeToggle = () => {
  const [lightMode, setLightMode] = useState(false);

  useEffect(() => {
    if (lightMode) {
      document.body.classList.add('light-theme');
    } else {
      document.body.classList.remove('light-theme');
    }
  }, [lightMode]);

  return (
    <button className="theme-toggle" onClick={() => setLightMode(!lightMode)}>
      {lightMode ? '🌙 Modo Oscuro' : '☀️ Modo Claro'}
    </button>
  );
};
