# 📝 To-Do List Manager (CLI) with Python, UV, and Click

Welcome to the To-Do List Manager, a simple and efficient Command-Line Interface (CLI) tool built using Python, managed with UV, and powered by Click for an interactive user experience.

This project allows you to efficiently manage your tasks directly from the terminal, making it lightweight and perfect for quick productivity!

## 🚀 Tech Stack

- **Python 🐍** - Core programming language
- **Click ⚡** - CLI framework for creating user-friendly commands
- **UV 🛠️**  - Fast package and environment manager for Python

  ## ✨ Features
  
- ✅ Add, view, and remove tasks effortlessly
- ✅ Mark tasks as completed and track progress
- ✅ List pending and completed tasks separately
- ✅ Persistent storage using JSON or text files
- ✅ Lightweight & Fast CLI tool for task management

## 🔧 Installation
1️⃣ Install uv (if not installed)

```bash
For Window:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex

Fo rmacOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
 ```
2️⃣ Install click (if not installed already)
```bash
uv add click
```
3️⃣ Clone the repository
```bash
git clone https://github.com/Muhammad-Fraooq/Todo_list_Python.git
cd Todo-list-Python
```
4️⃣ Set up a virtual environment
```bash
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows
```
 5️⃣ Create and Initialize the Project
 ```bash
uv init todo-cli
cd todo-cli
```
## 📌 Usage

Once installed, you can start using the To-Do List Manager from your terminal.
### 🔹 Add a new task
```bash
uv run python todo.py add "Finish the project"
```
### 🔹 View all tasks
```bash
uv run python todo.py show
```
### 🔹 Mark a task as completed
```bash
uv run python todo.py complete 1
```
### 🔹 Remove a task
```bash
uv run python todo.py delete 1
```
### Done task
```bash
uv run python todo.py done
```
## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project, feel free to fork the repo and submit a pull request. 😊

## 📜 License
This project is licensed under the MIT License.
