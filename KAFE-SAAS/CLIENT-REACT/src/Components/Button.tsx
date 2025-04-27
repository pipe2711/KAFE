type Props = {
  children: React.ReactNode;
  variant?: 'amber' | 'dark';
  onClick?: () => void;
  type?: 'submit' | 'button';
};

export const Button = ({ children, variant = 'amber', ...rest }: Props) => {
  return (
    <button className={`btn ${variant}`} {...rest}>
      {children}
    </button>
  );
};
