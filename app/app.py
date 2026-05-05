from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.datetime.now()
    return f"""
    Time: {now.strftime('%H:%M:%S')}
    Date: {now.strftime('%Y-%m-%d')}

    kal ki baten bhool ja , laura pakar k bhool ja
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
