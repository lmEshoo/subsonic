from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    subprocess.call("sh restart.sh", shell=True)
    return "Updated Music."

if __name__ == "__main__":
    subprocess.call("sh restart.sh", shell=True)
    app.run(host= '0.0.0.0', port='5000')
