# Put your app in here

from flask import Flask, request
from operations import add, sub, mult, div 

app = Flask(__name__)

@app.route('/')
def home_page():
    return "welcome to my calculator"

@app.route('/add')
def addition ():
    """ add a and b """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a + b)

@app.route('/sub')
def subtraction ():
    """ subtract a from b """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a - b)

@app.route('/mult')
def multiplication ():
    """ multiply a and b """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a * b)

@app.route('/div')
def division ():
    """divide a from b """
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(a / b)



# further study
math = {
    "add":add,
    "mult":mult,
    "sub":sub,
    "div":div
}
@app.route('/math/<operation>')
def math_oper (operation):
    """ addition, subtraction multiplication and division function """

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    
    return str(math[operation](a,b))

