import { useState, useEffect } from 'react';
import { ThemeToggle } from '../Components/ThemeToggle';

const Home: React.FC = () => {
  const [isDarkTheme, setIsDarkTheme] = useState(true);
  // Theme toggle function
  const toggleTheme = () => {
    setIsDarkTheme(!isDarkTheme);
  };
  // CSS Variables
  const theme = {
    dark: {
      bgColor: '#0f0f0f',
      textColor: '#eae6e1',
      navbarBg: '#1a1a1a',
      buttonBg: '#1a1a1a',
      buttonHover: '#4c413c',
      accent: '#dcd7d3',
      terminalBg: '#1a1a1a',
      terminalText: '#0f0',
    },
    light: {
      bgColor: '#eae6e1',
      textColor: '#1a1717',
      navbarBg: '#d1cdca',
      buttonBg: '#d1cdca',
      buttonHover: '#b9a89d',
      accent: '#221a21',
      terminalBg: '#fff',
      terminalText: '#333',
    }
  };
  const currentTheme = isDarkTheme ? theme.dark : theme.light;
  return (
    <div style={{
      backgroundColor: currentTheme.bgColor,
      color: currentTheme.textColor,
      fontFamily: 'system-ui, -apple-system, sans-serif',
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column',
    }}>
      {/* Header eliminado */}
      
      {/* Main Content */}
      <main style={{
        flex: 1,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '2rem 1rem',
      }}>
        <div style={{
          textAlign: 'center',
          maxWidth: '800px',
          marginBottom: '4rem',
        }}>
          <h1 style={{
            fontSize: 'calc(2rem + 2vw)',
            fontWeight: 800,
            marginBottom: '1.5rem',
            backgroundImage: isDarkTheme 
              ? 'linear-gradient(to right, #eae6e1, #dcd7d3)'
              : 'linear-gradient(to right, #1a1717, #221a21)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            backgroundClip: 'text',
          }}>
            KAFE
          </h1>
          <p style={{
            fontSize: 'calc(1rem + 0.5vw)',
            marginBottom: '0.5rem',
          }}>
            Deep Learning Language para todos
          </p>
          <p style={{
            fontSize: '1.125rem',
            opacity: 0.8,
            marginBottom: '2rem',
            maxWidth: '600px',
            margin: '0 auto 2rem',
          }}>
            Un lenguaje de programación intuitivo que facilita el aprendizaje y la creación de modelos de machine learning.
          </p>
          
          <div style={{
            display: 'flex',
            flexWrap: 'wrap',
            gap: '1rem',
            justifyContent: 'center',
            marginBottom: '2rem',
          }}>
            <a 
              href="/editor"
              style={{
                backgroundColor: currentTheme.accent,
                color: isDarkTheme ? currentTheme.bgColor : currentTheme.bgColor,
                padding: '0.75rem 1.5rem',
                borderRadius: '8px',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '1.125rem',
                boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
                transition: 'transform 0.2s ease, box-shadow 0.2s ease',
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.transform = 'translateY(-2px)';
                e.currentTarget.style.boxShadow = '0 6px 10px rgba(0, 0, 0, 0.15)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.transform = 'translateY(0)';
                e.currentTarget.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
              }}
            >
              Comenzar Ahora
            </a>
            
            <a 
              href="/docs"
              style={{
                backgroundColor: 'transparent',
                color: currentTheme.textColor,
                padding: '0.75rem 1.5rem',
                borderRadius: '8px',
                textDecoration: 'none',
                fontWeight: 600,
                fontSize: '1.125rem',
                border: `1px solid ${currentTheme.accent}`,
                transition: 'background-color 0.2s ease',
              }}
              onMouseOver={(e) => {
                e.currentTarget.style.backgroundColor = isDarkTheme 
                  ? 'rgba(220, 215, 211, 0.1)' 
                  : 'rgba(34, 26, 33, 0.1)';
              }}
              onMouseOut={(e) => {
                e.currentTarget.style.backgroundColor = 'transparent';
              }}
            >
              Ver Documentación
            </a>
            
            {/* Botón de cambio de tema usando la función toggleTheme existente */}
            <button 
              onClick={toggleTheme}
              style={{
                backgroundColor: currentTheme.buttonBg,
                color: currentTheme.textColor,
                border: 'none',
                borderRadius: '50%',
                width: '2.5rem',
                height: '2.5rem',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                cursor: 'pointer',
                fontSize: '1rem',
              }}
            >
              {isDarkTheme ? '☀️' : '🌙'}
            </button>
          </div>
        </div>
        
        {/* Code Example */}
        <div style={{
          width: '100%',
          maxWidth: '800px',
          marginBottom: '3rem',
          borderRadius: '12px',
          overflow: 'hidden',
          boxShadow: '0 8px 30px rgba(0, 0, 0, 0.12)',
        }}>
          <div style={{
            backgroundColor: isDarkTheme ? '#1a1a1a' : '#d1cdca',
            padding: '0.5rem',
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
          }}>
            <div style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: '#ff5f56' }}></div>
            <div style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: '#ffbd2e' }}></div>
            <div style={{ width: '12px', height: '12px', borderRadius: '50%', backgroundColor: '#27c93f' }}></div>
            <span style={{ marginLeft: '8px', fontSize: '0.875rem', opacity: 0.7 }}>ejemplo.kafe</span>
          </div>
          
          <pre style={{
            backgroundColor: currentTheme.terminalBg,
            color: currentTheme.terminalText,
            padding: '1.5rem',
            margin: 0,
            overflow: 'auto',
            fontFamily: 'monospace',
            fontSize: '0.9rem',
            lineHeight: 1.5,
          }}>
{`// Modelo de clasificación de imágenes simple en KAFE
modelo ImagenClasificador {
  entrada: Imagen(224, 224, 3)
  salida: Categoria(10)
  
  arquitectura {
    conv2d(32, 3, 3) -> relu -> maxpool(2, 2)
    conv2d(64, 3, 3) -> relu -> maxpool(2, 2)
    aplanar()
    denso(128) -> relu
    denso(10) -> softmax
  }
  
  entrenamiento {
    datos: ImagenesDataset
    optimizador: Adam(0.001)
    epocas: 10
    metricas: [precision, recall]
  }
}
// Ejecutar y evaluar el modelo
resultado = ImagenClasificador.entrenar()
print("Precisión del modelo: " + resultado.precision)`}
          </pre>
        </div>
        
        {/* Features */}
        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
          gap: '1.5rem',
          width: '100%',
          maxWidth: '1000px',
          marginBottom: '3rem',
        }}>
          {[
            { 
              title: "Intuitivo", 
              description: "Sintaxis clara y natural que acerca el Deep Learning a cualquier persona interesada en aprender.", 
              icon: "💡"
            },
            { 
              title: "Educativo", 
              description: "Diseñado para que estudiantes y profesores puedan entender y enseñar conceptos complejos de forma sencilla.", 
              icon: "🎓"
            },
            { 
              title: "Potente", 
              description: "Crea y entrena modelos complejos con menos código y mayor claridad sin sacrificar potencia.", 
              icon: "⚡"
            }
          ].map((feature, i) => (
            <div key={i} style={{
              backgroundColor: currentTheme.navbarBg,
              borderRadius: '12px',
              padding: '1.5rem',
              transition: 'transform 0.2s ease',
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.transform = 'translateY(-4px)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.transform = 'translateY(0)';
            }}>
              <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>{feature.icon}</div>
              <h3 style={{ fontSize: '1.25rem', fontWeight: 600, marginBottom: '0.5rem' }}>{feature.title}</h3>
              <p style={{ opacity: 0.8 }}>{feature.description}</p>
            </div>
          ))}
        </div>
      </main>
      
      {/* Footer */}
      <footer style={{
        padding: '2rem',
        textAlign: 'center',
        backgroundColor: currentTheme.navbarBg,
        color: currentTheme.textColor,
      }}>
        <p style={{ fontSize: '0.875rem', opacity: 0.7 }}>
          © {new Date().getFullYear()} KAFE Language • Creado con ❤️ para la comunidad de aprendizaje
        </p>
      </footer>
    </div>
  );
};
export default Home;