import { useEffect, useState } from "react";
import { getTasks, createTask, updateTask, deleteTask } from "./api";

import "./App.css";

function App() {
	const [tasks, setTasks] = useState([]);

	const [title, setTitle] = useState("");

	const [priority, setPriority] = useState("medium");

	const loadTasks = async () => {
		try {
			const res = await getTasks();

			setTasks(res.data);
		} catch (err) {
			console.error("Failed to load tasks", err);
		}
	};

	useEffect(() => {
		loadTasks();
	}, []);

	const handleAddTask = async () => {
		if (!title.trim()) return;

		try {
			await createTask({
				title,

				priority,
			});

			setTitle("");

			setPriority("medium");

			loadTasks();
		} catch (err) {
			console.error("Create failed", err);
		}
	};

	const handleComplete = async (task) => {
		try {
			await updateTask(task.id, {
				status: "completed",
			});

			loadTasks();
		} catch (err) {
			console.error("Update failed", err);
		}
	};

	const handleDelete = async (id) => {
		try {
			await deleteTask(id);

			loadTasks();
		} catch (err) {
			console.error("Delete failed", err);
		}
	};

	return (
		<div style={{ padding: "40px" }}>
			<h1>Task Manager</h1>

			{/* INPUT SECTION */}

			<div style={{ marginBottom: "20px" }}>
				<input
					type="text"
					placeholder="Enter task title"
					value={title}
					onChange={(e) => setTitle(e.target.value)}
				/>

				<select
					value={priority}
					onChange={(e) => setPriority(e.target.value)}
					style={{ marginLeft: "10px" }}
				>
					<option value="low">Low</option>

					<option value="medium">Medium</option>

					<option value="high">High</option>
				</select>

				<button onClick={handleAddTask} style={{ marginLeft: "10px" }}>
					Add Task
				</button>
			</div>

			{/* TABLE */}

			<table border="1" cellPadding="10">
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
					{tasks.length === 0 && (
						<tr>
							<td colSpan="6">No tasks yet</td>
						</tr>
					)}

					{tasks.map((task) => (
						<tr key={task.id}>
							<td>{task.id}</td>

							<td>{task.title}</td>

							<td>
								<span
									style={{
										color:
											task.status === "completed"
												? "green"
												: "orange",
									}}
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
										onClick={() => handleComplete(task)}
										style={{
											backgroundColor: "green",

											color: "white",

											marginRight: "5px",
										}}
									>
										Complete
									</button>
								)}

								<button
									onClick={() => handleDelete(task.id)}
									style={{
										backgroundColor: "red",

										color: "white",
									}}
								>
									Delete
								</button>
							</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
}

export default App;
