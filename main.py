""" Simple program to run a Caesar Cipher """

from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
        <!DOCTYPE html>

        <html>
            <head>
                <style>
                    form {{
                        background-color: #eee;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540px;
                        font: 16px sans-serif;
                        border-radius: 10px;
                    }}
                    textarea {{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>
            <body>
                <form method="POST">
                    <label for="rot">Rotate by:</label>
                    <input type="text" id="rot" name="rot" value="0">
                    <textarea id="text" name="text">{0}</textarea>
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """


@app.route("/")
def index():
    """ Runs the app """

    return form.format("")


@app.route("/", methods=['POST'])
def encrypt():
    """ Encrypts the string and returns it """

    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']

    return form.format(rotate_string(text, rot))

app.run()
