export default function Login() {
  return (
    <section className="login-page">
      <div className="login-card">
        <h2 className="login-title">Iniciar sesión</h2>
        <form className="login-form">
          <input type="email" placeholder="Correo institucional" required />
          <input type="password" placeholder="Contraseña" required />
          <button type="submit" className="btn amber">
            Entrar
          </button>
        </form>
      </div>
    </section>
  );
}
