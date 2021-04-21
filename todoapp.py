from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)
todolist = []
choices = ("low", "medium", "high")


@app.route('/')
def hello_world():
    return render_template('todo.html', todolist=todolist)


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    priority = request.form['priority']
    todoitem = [task, email, priority]
    x = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email)
    try:
        if x is None:
            return redirect('/')
        elif priority not in choices:
            return redirect('/')
        else:
            todolist.append(todoitem)
    except Exception as e:
        print(e)
    print(todolist)
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    todolist.clear()
    print(todolist)
    return redirect('/')


if __name__ == '__main__':
    app.run()
