import { useState, useEffect } from 'react';
import MonacoEditor from '@monaco-editor/react';
import Terminal from '../Components/Terminal';
import { EditorSideBar } from '../Components/EditorSideBar';
import EditorLayout from '../Components/EditorLayout';
import Modal from '../Components/Modal'; // Componente de modal reutilizable

export default function Editor() {
  // Estado que almacena los archivos abiertos en el editor
  const [files, setFiles] = useState<{ [key: string]: string }>({
    'main.kf': '// Código inicial',
  });

  // Estado que indica qué archivo está activo en el editor
  const [activeFile, setActiveFile] = useState('main.kf');

  // Estado para manejar el texto de salida de la terminal
  const [output, setOutput] = useState('$ ./main.kf\n');

  // Estado del tema del editor (oscuro o claro)
  const [theme, setTheme] = useState<'vs-dark' | 'vs-light'>('vs-dark');

  // Estado para mostrar el modal de confirmación al sobrescribir un archivo existente
  const [overwriteTarget, setOverwriteTarget] = useState<{ name: string; content: string } | null>(null);

  // Ejecutar el archivo actual enviando el código al backend
  const ejecutar = async () => {
    if (!activeFile || !files[activeFile]) return;

    try {
      const response = await fetch('http://149.130.179.251:5000/ejecutar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename: activeFile, code: files[activeFile] }),
      });

      const data = await response.json();
      setOutput((prev) => prev + (data.output || ' No se generó salida.') + '\n');
    } catch (error) {
      setOutput((prev) => prev + 'Error ejecutando el archivo.\n');
    }
  };

  // Detecta el tema del sistema (oscuro o claro) al cargar y cuando cambia
  useEffect(() => {
    const checkTheme = () => {
      setTheme(document.body.classList.contains('light-theme') ? 'vs-light' : 'vs-dark');
    };
    checkTheme();
    const observer = new MutationObserver(checkTheme);
    observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    return () => observer.disconnect();
  }, []);

  // Maneja los cambios de texto dentro del editor Monaco
  const handleCodeChange = (val: string | undefined) => {
    setFiles({ ...files, [activeFile]: val || '' });
  };

  // Agrega un nuevo archivo vacío y lo activa
  const createFile = (filename: string) => {
    setFiles((prev) => ({ ...prev, [filename]: '' }));
    setActiveFile(filename);
  };

  // Elimina un archivo del estado
  const deleteFile = (filename: string) => {
    const updated = { ...files };
    delete updated[filename];
    const fallback = Object.keys(updated)[0] || '';
    setFiles(updated);
    setActiveFile(fallback);
  };

  // Renombra un archivo manteniendo su contenido
  const renameFile = (oldName: string, newName: string) => {
    setFiles((prev) => {
      const { [oldName]: content, ...rest } = prev;
      return { ...rest, [newName]: content };
    });
    if (activeFile === oldName) setActiveFile(newName);
  };

  // Lógica para importar un archivo externo al editor
  const handleFileImport = (filename: string, content: string) => {
    if (files[filename]) {
      // Si el archivo ya existe, muestra modal para confirmar sobrescritura
      setOverwriteTarget({ name: filename, content });
    } else {
      // Si no existe, se agrega directamente
      setFiles((prev) => ({ ...prev, [filename]: content }));
      setActiveFile(filename);
    }
  };

  return (
    <div style={{ height: '100vh', display: 'flex' }}>
      {/* Barra lateral para crear, seleccionar, renombrar y eliminar archivos */}
      <EditorSideBar
        files={files}
        activeFile={activeFile}
        onFileSelect={setActiveFile}
        onFileCreate={createFile}
        onFileDelete={deleteFile}
        onFileRename={renameFile}
        onFileImport={handleFileImport}
      />

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        {/* Barra superior con el botón "Ejecutar" */}
        <div
          style={{
            padding: '0.5rem',
            background: theme === 'vs-dark' ? '#222' : '#eee',
            borderBottom: '1px solid #444',
          }}
        >
          <button
            onClick={ejecutar}
            style={{
              backgroundColor: '#2ecc71',
              color: 'white',
              padding: '0.5rem 1rem',
              border: 'none',
              borderRadius: '4px',
              fontWeight: 'bold',
              cursor: 'pointer',
            }}
          >
            Ejecutar
          </button>
        </div>

        {/* Contenedor que muestra el editor de código y la terminal de salida */}
        <EditorLayout>
          <div style={{ width: '100%', height: '100%', overflow: 'hidden' }}>
            <MonacoEditor
              height="100%"
              language="plaintext"
              theme={theme}
              value={files[activeFile]}
              onChange={handleCodeChange}
              options={{
                fontSize: 14,
                minimap: { enabled: false },
                automaticLayout: true,
              }}
            />
          </div>

          <div style={{ height: '100%' }}>
            <Terminal output={output} />
          </div>
        </EditorLayout>
      </div>

      {/* Modal personalizado que aparece si se intenta sobrescribir un archivo ya existente */}
      {overwriteTarget && (
        <Modal
          isOpen={true}
          title={`El archivo "${overwriteTarget.name}" ya existe`}
          onCancel={() => setOverwriteTarget(null)}
          onConfirm={() => {
            setFiles((prev) => ({
              ...prev,
              [overwriteTarget.name]: overwriteTarget.content,
            }));
            setActiveFile(overwriteTarget.name);
            setOverwriteTarget(null);
          }}
          confirmText="Sobrescribir"
          cancelText="Cancelar"
        >
          <p style={{ color: '#ccc' }}>
            Este grano ya fue tostado. ¿Deseas reemplazar su aroma con uno nuevo?
          </p>
        </Modal>
      )}
    </div>
  );
}
