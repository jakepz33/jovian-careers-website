from flask import Flask

app = Flask(__name__)

# when the URL "/" is accessed, show Hello World
@app.route("/")
def hellow_world():
    return "Hello World"

print(__name__)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) #provide a host 
