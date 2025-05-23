import { useEffect } from 'react';
import Split from 'split.js';

interface Props {
  children: React.ReactNode[];
}

export default function EditorLayout({ children }: Props) {
  useEffect(() => {
    Split(['#editor-pane', '#terminal-pane'], {
      direction: 'vertical',
      sizes: [75, 25],
      gutterSize: 8,
      minSize: 100,
      cursor: 'row-resize',
      gutter: (index, direction) => {
        const gutter = document.createElement('div');
        gutter.className = `gutter gutter-${direction}`;
        return gutter;
      },
    });
  }, []);

  return (
    <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
      <div id="editor-pane" style={{ height: '100%', overflow: 'hidden' }}>
        {children[0]}
      </div>
      <div id="terminal-pane" style={{ height: '30%', overflow: 'auto' }}>
        {children[1]}
      </div>
    </div>
  );
}
