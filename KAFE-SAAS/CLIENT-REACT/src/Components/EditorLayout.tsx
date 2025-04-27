import { useEffect } from 'react';
import Split from 'split.js';

export default function EditorLayout({
  children,
}: {
  children: React.ReactNode[];
}) {
  useEffect(() => {
    const panes = document.querySelectorAll('#editor-pane, #terminal-pane');
    if (panes.length === 2) {
      Split(['#editor-pane', '#terminal-pane'], {
        direction: 'vertical',
        sizes: [75, 25],
        gutterSize: 6,
        minSize: 100,
        cursor: 'row-resize',
      });
    }
  }, []);

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div id="editor-pane" style={{ flexGrow: 1, overflow: 'hidden' }}>
        {children[0]}
      </div>
      <div id="terminal-pane" style={{ height: '30%', overflow: 'auto' }}>
        {children[1]}
      </div>
    </div>
  );
}
