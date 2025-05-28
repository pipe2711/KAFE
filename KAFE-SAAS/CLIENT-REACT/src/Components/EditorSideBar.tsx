import { useState } from 'react';
import { Plus, Trash2, Pencil, Upload, Download } from 'lucide-react';
import Modal from './Modal';

interface Props {
  files: { [key: string]: string };
  activeFile: string;
  onFileSelect: (filename: string) => void;
  onFileCreate: (filename: string) => void;
  onFileDelete: (filename: string) => void;
  onFileRename: (oldName: string, newName: string) => void;
  onFileImport?: (filename: string, content: string) => void;
  archivosTxt?: string[];
}

export const EditorSideBar = ({
  files,
  activeFile,
  onFileSelect,
  onFileCreate,
  onFileDelete,
  onFileRename,
  onFileImport,
  archivosTxt = [],
}: Props) => {
  const [newFileName, setNewFileName] = useState('');
  const [renameTarget, setRenameTarget] = useState<string | null>(null);
  const [newName, setNewName] = useState('');
  const [deleteTarget, setDeleteTarget] = useState<string | null>(null);
  const [overwriteTarget, setOverwriteTarget] = useState<{ name: string; content: string } | null>(null);

  const handleNewFile = () => {
    if (newFileName.trim() && !files[newFileName]) {
      onFileCreate(newFileName.trim());
      setNewFileName('');
    }
  };

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    const content = await file.text();

    if (files[file.name]) {
      setOverwriteTarget({ name: file.name, content });
    } else {
      onFileImport?.(file.name, content);
    }

    e.target.value = '';
  };

  const handleDownload = () => {
    const content = files[activeFile];
    const blob = new Blob([content], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = activeFile;
    a.click();
    URL.revokeObjectURL(url);
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem' }}>
          <span style={{ fontWeight: 'bold' }}>Archivos</span>

          <div style={{ display: 'flex', gap: '0.3rem', marginLeft: 'auto' }}>
            <label htmlFor="file-upload" style={{ cursor: 'pointer', padding: '0.2rem' }}>
              <span title="Subir archivo">
                <Upload size={16} />
              </span>
              <input
                id="file-upload"
                type="file"
                accept=".kf"
                style={{ display: 'none' }}
                onChange={handleUpload}
              />
            </label>

            <button
              onClick={handleDownload}
              style={{
                background: 'none',
                border: 'none',
                cursor: 'pointer',
                padding: '0.2rem',
              }}
            >
              <span title="Descargar archivo">
                <Download size={16} />
              </span>
            </button>
          </div>
        </div>

        <div style={{ marginTop: '0.5rem', display: 'flex', gap: '0.5rem' }}>
          <input
            type="text"
            value={newFileName}
            onChange={(e) => setNewFileName(e.target.value)}
            placeholder="nuevo.kf"
            style={{ flexGrow: 1, fontSize: '0.85rem', padding: '0.3rem' }}
          />
          <button onClick={handleNewFile}>
            <Plus size={16} />
          </button>
        </div>
      </div>

      <ul className="file-list" style={{ marginTop: '0.75rem' }}>
        {Object.keys(files).map((file) => (
          <li
            key={file}
            className={`file-item ${file === activeFile ? 'active' : ''}`}
            onClick={() => onFileSelect(file)}
          >
            {file}
            <span style={{ float: 'right', display: 'flex', gap: '0.5rem' }}>
              <Pencil
                size={14}
                style={{ cursor: 'pointer' }}
                onClick={(e) => {
                  e.stopPropagation();
                  setRenameTarget(file);
                  setNewName(file);
                }}
              />
              <Trash2
                size={14}
                style={{ cursor: 'pointer', color: '#c44' }}
                onClick={(e) => {
                  e.stopPropagation();
                  setDeleteTarget(file);
                }}
              />
            </span>
          </li>
        ))}
      </ul>

      {archivosTxt.length > 0 && (
        <ul className="file-list" style={{ marginTop: '1rem' }}>
          <strong style={{ marginLeft: '0.5rem' }}>Archivos .txt</strong>
          {archivosTxt.map((file) => (
            <li
              key={file}
              className="file-item"
              style={{ paddingLeft: '1rem', fontStyle: 'italic', cursor: 'pointer' }}
              onClick={() => {
                const programa = activeFile.replace('.kf', '');
                const url = `http://149.130.179.251:5000/archivo_usuario/${programa}/${file}`;
                const a = document.createElement('a');
                a.href = url;
                a.download = file;
                a.click();
              }}
            >
              📄 {file}
            </li>
          ))}
        </ul>
      )}

      {/* Modal para renombrar */}
      <Modal
        isOpen={renameTarget !== null}
        title="Renombrar archivo"
        onCancel={() => setRenameTarget(null)}
        onConfirm={() => {
          if (renameTarget && newName.trim() && !files[newName]) {
            onFileRename(renameTarget, newName.trim());
          }
          setRenameTarget(null);
        }}
        confirmText="Renombrar"
      >
        <p style={{ color: '#ccc', marginBottom: '1rem' }}>
          Dale un nuevo aroma a tu código. Renombra este archivo con estilo KAFE.
        </p>
        <input
          type="text"
          value={newName}
          onChange={(e) => setNewName(e.target.value)}
          style={{
            width: '100%',
            padding: '0.5rem',
            borderRadius: '5px',
            border: '1px solid #ccc',
            backgroundColor: '#2c2c2c',
            color: 'white',
          }}
        />
      </Modal>

      {/* Modal para confirmar eliminación */}
      <Modal
        isOpen={deleteTarget !== null}
        title={`¿Eliminar archivo "${deleteTarget}"?`}
        onCancel={() => setDeleteTarget(null)}
        onConfirm={() => {
          if (deleteTarget) onFileDelete(deleteTarget);
          setDeleteTarget(null);
        }}
        confirmText="Eliminar"
        cancelText="Cancelar"
      >
        <p style={{ color: '#ccc' }}>
          Algunos granos deben desecharse para obtener un mejor café. ¿Seguro que deseas eliminar este archivo?
        </p>
      </Modal>

      {/* Modal para sobrescribir archivo */}
      <Modal
        isOpen={overwriteTarget !== null}
        title={`El archivo "${overwriteTarget?.name}" ya existe`}
        onCancel={() => setOverwriteTarget(null)}
        onConfirm={() => {
          if (overwriteTarget) {
            onFileImport?.(overwriteTarget.name, overwriteTarget.content);
            setOverwriteTarget(null);
          }
        }}
        confirmText="Sobrescribir"
        cancelText="Cancelar"
      >
        <p style={{ color: '#ccc' }}>
          Este grano ya fue tostado. ¿Deseas reemplazar su aroma con uno nuevo?
        </p>
      </Modal>
    </aside>
  );
};
