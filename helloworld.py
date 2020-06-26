from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

@app.route('/')
@app.route('/home')
def home():
    return "Home Page"

@app.route('/test')
def hello():
    return render_template('test.html')

@app.route('/index')
def index():
    user = {'username': {'firstname': 'Gergo'}}
    return render_template('tt.html', user=user)

@app.route('/users/<string:name>/age/<int:age>')
def variable(name, age):
    return "Hello, {}! You are {} years old.".format(name.title(), age)

@app.route('/onlyget', methods=['POST', 'GET'])
def onlyget():
    return "This page is GET only."

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

if __name__ == "__main__":
    app.run(debug=True)
