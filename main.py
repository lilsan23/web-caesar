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
        <form action="/" method="post">
        <label for='rot'> Rotate by: </label>
            <input id='rot' type="text" name ='rot' value=0 />
            <textarea id='text' name='Text' rows='10' col='10'></textarea>
            <input type='submit' name='Submit Query'/>
        </form>
    </body>
</html>
"""return user_input_rot

@app.route("/")
def index():
    return form

@app.route("/", methods=['POST'])
def encrypt():
    #user_input_rot = request.form['rot']
    #user_text = request.form['text']
    #encrypt_msg = rotate_string(user_text,user_input_rot)
   # return  '<h1>' user_input_rot '</h1>'
app.run()