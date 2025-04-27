import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Navbar } from './Components/Navbar';
import Home from './Pages/Home';
import Editor from './Pages/Editor';
import Docs from './Pages/Docs';
import Login from './Pages/Login';
import { ThemeToggle } from './Components/ThemeToggle';


export default function App() {

  return (
    <Router>
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/editor" element={<Editor />} />
          <Route path="/docs" element={<Docs />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </main>
      <ThemeToggle /> {/* Aquí se monta en todas las vistas */}
    </Router>
  );
}
