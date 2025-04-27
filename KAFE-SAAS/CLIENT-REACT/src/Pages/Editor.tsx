import { useState, useEffect } from 'react';
import MonacoEditor from '@monaco-editor/react';
import Terminal from '../Components/Terminal';
import { EditorSideBar } from '../Components/EditorSideBar';

export default function Editor() {
  const [files, setFiles] = useState<{ [key: string]: string }>({
    'main.kf': '// Código inicial',
  });

  const [activeFile, setActiveFile] = useState('main.kf');
  const [output, setOutput] = useState('$ ./main.kf\n');
  const [theme, setTheme] = useState<'vs-dark' | 'vs-light'>('vs-dark');

  const ejecutar = () => {
    const simulatedOutput = `$ ./run ${activeFile}\n✔ Output generado: ${files[activeFile].length} caracteres\n`;
    setOutput((prev) => prev + simulatedOutput);
  };

  useEffect(() => {
    const checkTheme = () => {
      setTheme(
        document.body.classList.contains('light-theme') ? 'vs-light' : 'vs-dark'
      );
    };
    checkTheme();
    const observer = new MutationObserver(checkTheme);
    observer.observe(document.body, {
      attributes: true,
      attributeFilter: ['class'],
    });
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

    const remaining = Object.keys(updated);
    const fallback = remaining.length > 0 ? remaining[0] : '';
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

  return (
    <div style={{ height: '100vh', display: 'flex' }}>
      <EditorSideBar
        files={files}
        activeFile={activeFile}
        onFileSelect={setActiveFile}
        onFileCreate={createFile}
        onFileDelete={deleteFile}
        onFileRename={renameFile}
      />

      <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
        <div style={{ flexGrow: 1 }}>
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

        <div
          style={{
            padding: '0.5rem',
            background: theme === 'vs-dark' ? '#222' : '#eee',
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

        <div style={{ height: '25vh' }}>
          <Terminal output={output} />
        </div>
      </div>
    </div>
  );
}
