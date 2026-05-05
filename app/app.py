from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"""
    <html>
    <head>
        <title>Digital Clock</title>
        <meta http-equiv="refresh" content="1">
        <style>
            body {{
                background-color: black;
                color: lime;
                font-family: monospace;
                text-align: center;
                margin-top: 20%;
            }}
            .clock {{
                font-size: 60px;
            }}
            .date {{
                font-size: 30px;
            }}
        </style>
    </head>
    <body>
        <div class="clock">{now.strftime('%H:%M:%S')}</div>
        <div class="date">{now.strftime('%Y-%m-%d')}</div>
        <br>
        🚀 CI/CD Digital Clock v3 🚀
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
