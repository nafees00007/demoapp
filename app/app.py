from flask import Flask
import socket
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    🚀 CI/CD SUCCESSFUL 🚀 <br><br>
    Version: v2 <br>
    Deployed at: {datetime.datetime.now()} <br>
    Hostname: {socket.gethostname()} <br>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
