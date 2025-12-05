from flask import Flask

app = Flask(__name__)


# routes
@app.get("/")
def root():
    return "<h1>Hello, World!!!</h1><h2>Hello, Galaxy!!!</h2>"


@app.get("/home")
def home_page():
    return "<h1>Home Page</h1>"


@app.get("/about")
def about_page():
    return "<h1>About Us</h1>"


# we can make the same function get execute on multiple routes
@app.get("/contact-us")
@app.get("/contact")
def contact():
    return "<h1>Contact Us</h1>"


if __name__ == "__main__":
    app.run(debug=True)
