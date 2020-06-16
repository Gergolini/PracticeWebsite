from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Home Page"

@app.route('/test')
def hello():
    return render_template('test.html')

@app.route('/manyheaders')
def manyheaders():
    return render_template('tt.html')

@app.route('/users/<string:name>/age/<int:age>')
def variable(name, age):
    return "Hello, {}! You are {} years old.".format(name.title(), age)

@app.route('/onlyget', methods=['POST', 'GET'])
def onlyget():
    return "This page is GET only."

if __name__ == "__main__":
    app.run(debug=True)
