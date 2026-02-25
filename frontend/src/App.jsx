import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "./api";

function App() {
	const [tasks, setTasks] = useState([]);
	const [title, setTitle] = useState("");

	const loadTasks = async () => {
		const res = await getTasks();
		setTasks(res.data);
	};

	useEffect(() => {
		loadTasks();
	}, []);

	const handleCreate = async () => {
		if (!title.trim()) return;

		await createTask({
			title,
			priority: "medium",
		});

		setTitle("");
		loadTasks();
	};

	const markComplete = async (task) => {
		await updateTask(task.id, {
			status: "completed",
		});

		loadTasks();
	};

	const handleDelete = async (id) => {
		await deleteTask(id);
		loadTasks();
	};

	return (
		<div style={{ padding: 20 }}>
			<h1>Task Manager</h1>

			<div>
				<input
					value={title}
					onChange={(e) => setTitle(e.target.value)}
					placeholder="Task title"
				/>

				<button onClick={handleCreate}>Add</button>
			</div>

			<ul>
				{tasks.map((task) => (
					<li key={task.id}>
						{task.title} — {task.status}
						{task.status !== "completed" && (
							<button onClick={() => markComplete(task)}>
								Complete
							</button>
						)}
						<button onClick={() => handleDelete(task.id)}>
							Delete
						</button>
					</li>
				))}
			</ul>
		</div>
	);
}

export default App;
