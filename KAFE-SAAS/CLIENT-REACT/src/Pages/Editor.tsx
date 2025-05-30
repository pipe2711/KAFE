import { useState, useEffect } from 'react';
import MonacoEditor from '@monaco-editor/react';
import Terminal from '../Components/Terminal';
import { EditorSideBar } from '../Components/EditorSideBar';
import EditorLayout from '../Components/EditorLayout';
import Modal from '../Components/Modal';

export default function Editor() {
  const [files, setFiles] = useState<{ [key: string]: string }>({
    'main.kf': '// Código inicial',
  });

  const [activeFile, setActiveFile] = useState('main.kf');
  const [output, setOutput] = useState('$ ./main.kf\n');
  const [theme, setTheme] = useState<'vs-dark' | 'vs-light'>('vs-dark');
  const [overwriteTarget, setOverwriteTarget] = useState<{ name: string; content: string } | null>(null);
  const [svgUrl, setSvgUrl] = useState<string | null>(null);
  const [showGraphModal, setShowGraphModal] = useState(false);

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

      if (data.svg_name && typeof data.svg_name === 'string') {
        setSvgUrl(`http://149.130.179.251:5000/static/${data.svg_name}`);
        setShowGraphModal(true);
      } else {
        setSvgUrl(null);
        setShowGraphModal(false);
      }
    } catch (error) {
      setOutput((prev) => prev + 'Error ejecutando el archivo.\n');
      setSvgUrl(null);
      setShowGraphModal(false);
    }
  };

  useEffect(() => {
    const checkTheme = () => {
      setTheme(document.body.classList.contains('light-theme') ? 'vs-light' : 'vs-dark');
    };
    checkTheme();
    const observer = new MutationObserver(checkTheme);
    observer.observe(document.body, { attributes: true, attributeFilter: ['class'] });
    return () => observer.disconnect();
  }, []);

  const handleCodeChange = (val: string | undefined) => {
    setFiles({ ...files, [activeFile]: val || '' });
  };

  const createFile = (filename: string) => {
    setFiles((prev) => ({ ...prev, [filename]: '' }));
    setActiveFile(filename);
  };

  const deleteFile = (filename: string) => {
    const updated = { ...files };
    delete updated[filename];
    const fallback = Object.keys(updated)[0] || '';
    setFiles(updated);
    setActiveFile(fallback);
  };

  const renameFile = (oldName: string, newName: string) => {
    setFiles((prev) => {
      const { [oldName]: content, ...rest } = prev;
      return { ...rest, [newName]: content };
    });
    if (activeFile === oldName) setActiveFile(newName);
  };

  const handleFileImport = (filename: string, content: string) => {
    if (files[filename]) {
      setOverwriteTarget({ name: filename, content });
    } else {
      setFiles((prev) => ({ ...prev, [filename]: content }));
      setActiveFile(filename);
    }
  };

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (event.ctrlKey && event.key.toLowerCase() === 'l') {
        event.preventDefault();
        setOutput('$ ./main.kf\n');
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div style={{ height: '100vh', display: 'flex' }}>
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

          <Terminal output={output} />
        </EditorLayout>
      </div>

      {/* Modal de confirmación para sobrescribir archivos */}
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

      {/* Modal para mostrar gráfico */}
      {svgUrl && showGraphModal && (
        <Modal
          isOpen={true}
          title="📈 Gráfico generado"
          onCancel={() => setShowGraphModal(false)}
          onConfirm={() => setShowGraphModal(false)}
          confirmText="Cerrar"
          cancelText=""
        >
          <img
            src={svgUrl}
            alt="Gráfico generado"
            style={{
              maxWidth: '100%',
              maxHeight: '70vh',
              border: '1px solid #444',
              background: '#fff',
              padding: '0.5rem',
            }}
          />
        </Modal>
      )}
    </div>
  );
}
