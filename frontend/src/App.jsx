import { useEffect, useState } from "react";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  // Fetch tasks from backend
  const fetchTasks = () => {
    fetch("http://127.0.0.1:5000/api/tasks")
      .then((res) => res.json())
      .then((data) => setTasks(data.tasks))
      .catch((err) => console.error("Error:", err));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  // Add new task to backend
  const addTask = () => {
    if (!newTask.trim()) return;

    fetch("http://127.0.0.1:5000/api/tasks", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name: newTask }),
    })
      .then((res) => res.json())
      .then((data) => {
        setTasks([...tasks, data]);
        setNewTask("");
      })
      .catch((err) => console.error("Error:", err));
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>🧩 Flask + React Full Connection</h1>

      <div style={{ marginBottom: "1rem" }}>
        <input
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Enter new task"
          style={{ padding: "0.5rem" }}
        />
        <button onClick={addTask} style={{ marginLeft: "0.5rem", padding: "0.5rem" }}>
          Add Task
        </button>
      </div>

      <ul>
        {tasks.map((t) => (
          <li key={t.id}>{t.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
