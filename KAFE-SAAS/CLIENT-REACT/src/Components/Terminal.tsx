import React from 'react';

interface TerminalProps {
  output: string;
}

const Terminal: React.FC<TerminalProps> = ({ output }) => {
  return (
    <div className="terminal-output">
      <pre>{output}</pre>
    </div>
  );
};

export default Terminal;
