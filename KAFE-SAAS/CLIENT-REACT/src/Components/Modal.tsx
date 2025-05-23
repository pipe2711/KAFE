import React from 'react';

interface ModalProps {
  isOpen: boolean;
  title: string;
  children: React.ReactNode;
  onCancel: () => void;
  onConfirm?: () => void;
  confirmText?: string;
  cancelText?: string;
}

export default function Modal({
  isOpen,
  title,
  children,
  onCancel,
  onConfirm,
  confirmText = 'Aceptar',
  cancelText = 'Cancelar',
}: ModalProps) {
  if (!isOpen) return null;

  return (
    <div style={overlayStyle}>
      <div style={modalStyle}>
        <h3 style={{ marginBottom: '1rem' }}>{title}</h3>
        {children}
        <div style={{ marginTop: '1.5rem', display: 'flex', justifyContent: 'flex-end', gap: '0.5rem' }}>
          <button onClick={onCancel} style={buttonCancelStyle}>
            {cancelText}
          </button>
          {onConfirm && (
            <button onClick={onConfirm} style={buttonConfirmStyle}>
              {confirmText}
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

// Estilos inline básicos
const overlayStyle: React.CSSProperties = {
  position: 'fixed',
  top: 0,
  left: 0,
  width: '100vw',
  height: '100vh',
  backgroundColor: 'rgba(0, 0, 0, 0.6)',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  zIndex: 9999,
};

const modalStyle: React.CSSProperties = {
  backgroundColor: '#1a1a1a',
  color: '#fff',
  padding: '2rem',
  borderRadius: '10px',
  minWidth: '300px',
};

const buttonCancelStyle: React.CSSProperties = {
  backgroundColor: '#555',
  color: 'white',
  padding: '0.4rem 1rem',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
};

const buttonConfirmStyle: React.CSSProperties = {
  backgroundColor: '#2ecc71',
  color: 'white',
  padding: '0.4rem 1rem',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
};
