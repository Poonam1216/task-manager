import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "./api";
import "./App.css";

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

	const handleComplete = async (task) => {
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
		<div className="container">
			<h1>Task Manager</h1>

			<div className="form">
				<input
					value={title}
					onChange={(e) => setTitle(e.target.value)}
					placeholder="Enter task title"
				/>

				<button onClick={handleCreate}>Add Task</button>
			</div>

			<table>
				<thead>
					<tr>
						<th>ID</th>
						<th>Title</th>
						<th>Status</th>
						<th>Priority</th>
						<th>Created</th>
						<th>Actions</th>
					</tr>
				</thead>

				<tbody>
					{tasks.length === 0 ? (
						<tr>
							<td colSpan="6">No tasks yet</td>
						</tr>
					) : (
						tasks.map((task) => (
							<tr key={task.id}>
								<td>{task.id}</td>

								<td>{task.title}</td>

								<td>
									<span
										className={
											task.status === "completed"
												? "status done"
												: "status pending"
										}
									>
										{task.status}
									</span>
								</td>

								<td>{task.priority}</td>

								<td>
									{new Date(task.created_at).toLocaleString()}
								</td>

								<td>
									{task.status !== "completed" && (
										<button
											className="complete"
											onClick={() => handleComplete(task)}
										>
											Complete
										</button>
									)}

									<button
										className="delete"
										onClick={() => handleDelete(task.id)}
									>
										Delete
									</button>
								</td>
							</tr>
						))
					)}
				</tbody>
			</table>
		</div>
	);
}

export default App;
