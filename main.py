from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["Debug"] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }

            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form>
        <label for='rot'> Rotate by: </label>
            <input id='rot' type="text" name ='rot' value=0 />
            <textarea id='text' name='Text' rows='10' col='10'></textarea>
            <input type='submit' name='Submit Query'/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@pp.route("/", methods=['Post'])
def encrypt(rot):
    user_input = rot

app.run()