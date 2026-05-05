from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Simple Message</title>
        <meta http-equiv="refresh" content="2">
        <style>
            body {
                background-color: yellow;
                color: black;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 20%;
                font-size: 40px;
            }
        </style>
    </head>
    <body>
        Kal ki baten bhool ja, Lauda pakar k jhool ja
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
