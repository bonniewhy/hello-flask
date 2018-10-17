from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True


tasks = []


@app.route('/', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST': # This is case sensitive!!
        task = request.form['task']
        tasks.append(task)


    template = jinja_env.get_template('todos.html')
    return template.render(tasks=tasks, title="I have so much TODO...")

app.run()