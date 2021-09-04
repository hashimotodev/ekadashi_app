import logo from "./logo.svg";
import "./App.css";

function App() {
  function ola() {
    alert("Oi!");
  }
  return (
    <div className="App">
      <button type="submit" onclick="ola()">
        Clique aqui
      </button>
    </div>
  );
}

export default App;
