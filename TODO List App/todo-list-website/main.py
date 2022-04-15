from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap


def main():
    app = Flask(__name__)
    Bootstrap(app)

    todo_list = {
        "tasks": [

        ]
    }

    @app.route('/', methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            form = request.form

            name = form["name"]
            description = form["message"]

            task = {
                "id": len(todo_list["tasks"]),
                "name": name,
                "description": description,
                "completed": False,
            }

            todo_list["tasks"].append(task)
        return render_template("index.html", tasks=todo_list["tasks"])

    @app.route('/complete-task')
    def mark_task_completed():
        task = int(request.args.get("task_id"))
        todo_list["tasks"][task]["completed"] = True

        return redirect(url_for('home'))

    if __name__ == "__main__":
        app.run(debug=True)


main()
