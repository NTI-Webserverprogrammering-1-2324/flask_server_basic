# 1. Import the Flask class from the flask module
from flask import Flask

# 2. Create an instance of the Flask class
app = Flask(__name__)


# 3. Define a route and a view function
@app.route("/")
def hello():
    return "Hello World!"


# 4. Run the application
if __name__ == "__main__":
    app.run(debug=True, port=3000)
