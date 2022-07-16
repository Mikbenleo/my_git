from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Word!"

app.run('0.0.0.0', 8000)


#   from flask import Flask
# ModuleNotFoundError: No module named 'flask'
#
# C:\Users\mikbe\Pycharm\skypro_lesson_10_2\venv>pip freeze

# Flask==2.1.3

# Jinja2==3.1.2
# MarkupSafe==2.1.1
# requests==2.28.0

# Werkzeug==2.1.2


