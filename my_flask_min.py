from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Word!"

app.run('0.0.0.0', 8000)


  from flask import Flask
ModuleNotFoundError: No module named 'flask'





