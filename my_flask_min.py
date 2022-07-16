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
# certifi==2022.6.15
# charset-normalizer==2.0.12
# click==8.1.3
# colorama==0.4.5
# Flask==2.1.3
# idna==3.3
# itsdangerous==2.1.2
# Jinja2==3.1.2
# MarkupSafe==2.1.1
# requests==2.28.0
# urllib3==1.26.9
# Werkzeug==2.1.2


