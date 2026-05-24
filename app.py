from flask import Flask, render_template, request, redirect

app = Flask(__name__)

TASK_FILE = "tasks.txt"

# Read tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Save task to file
def save_task(task):
    with open(TASK_FILE, "a") as file:
        file.write(task + "\n")

# Delete task
def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)

    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")

        if task:
            save_task(task)

        return redirect("/")

    tasks = load_tasks()

    return render_template("index.html", tasks=tasks)

# Delete route
@app.route("/delete/<int:index>")
def delete(index):
    delete_task(index)
    return redirect("/")

if __name__ == "__main__":
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)