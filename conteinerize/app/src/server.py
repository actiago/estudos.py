"""from flask import Flask
server = Flask(__name__)

@server.route("/")
 def hello():
    return "Hello World!"

if __name__ == "__main__":
   server.run()
"""

# Copy from https://github.com/chcdc/flask-demo-app

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
        return "It's working!\n"

