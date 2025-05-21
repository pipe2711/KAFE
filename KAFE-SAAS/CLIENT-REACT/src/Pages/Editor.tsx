import { useState, useEffect } from 'react';
import MonacoEditor from '@monaco-editor/react';
import Terminal from '../Components/Terminal';
import { EditorSideBar } from '../Components/EditorSideBar';
import EditorLayout from '../Components/EditorLayout';

export default function Editor() {
  const [files, setFiles] = useState<{ [key: string]: string }>({
    'main.kf': '// Código inicial',
  });

  const [activeFile, setActiveFile] = useState('main.kf');
  const [output, setOutput] = useState('$ ./main.kf\n');
  const [theme, setTheme] = useState<'vs-dark' | 'vs-light'>('vs-dark');

  const ejecutar = async () => {
    if (!activeFile || !files[activeFile]) return;

    try {
      const response = await fetch('http://localhost:5000/ejecutar', {
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
    setFiles((prev) => {
      if (prev[filename]) {
        const overwrite = confirm(`El archivo "${filename}" ya existe. ¿Deseas sobrescribirlo?`);
        if (!overwrite) return prev;
      }
      return { ...prev, [filename]: content };
    });
    setActiveFile(filename);
  };

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

          <div style={{ height: '100%' }}>
            <Terminal output={output} />
          </div>
        </EditorLayout>
      </div>
    </div>
  );
}
