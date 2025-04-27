import { useState } from 'react';
import { Plus, Trash2, Pencil } from 'lucide-react';

interface Props {
  files: { [key: string]: string };
  activeFile: string;
  onFileSelect: (filename: string) => void;
  onFileCreate: (filename: string) => void;
  onFileDelete: (filename: string) => void;
  onFileRename: (oldName: string, newName: string) => void;
}

export const EditorSideBar = ({
  files,
  activeFile,
  onFileSelect,
  onFileCreate,
  onFileDelete,
  onFileRename,
}: Props) => {
  const [newFileName, setNewFileName] = useState('');

  const handleNewFile = () => {
    if (newFileName.trim() && !files[newFileName]) {
      onFileCreate(newFileName.trim());
      setNewFileName('');
    }
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-header">
        Archivos
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
      <ul className="file-list">
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
                  const newName = prompt('Nuevo nombre para el archivo:', file);
                  if (newName && newName !== file && !files[newName]) {
                    onFileRename(file, newName);
                  }
                }}
              />
              <Trash2
                size={14}
                style={{ cursor: 'pointer', color: '#c44' }}
                onClick={(e) => {
                  e.stopPropagation();
                  const confirmDelete = confirm(`¿Eliminar ${file}?`);
                  if (confirmDelete) onFileDelete(file);
                }}
              />
            </span>
          </li>
        ))}
      </ul>
    </aside>
  );
};
