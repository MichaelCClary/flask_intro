from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{add(a, b)}"


@app.route("/sub")
def sub_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{sub(a, b)}"


@app.route("/mult")
def mult_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{mult(a, b)}"


@app.route("/div")
def div_route():
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{div(a, b)}"


@app.route("/math/<oper>")
def math_route(oper):
    a = int(request.args["a"])
    b = int(request.args["b"])

    math = {
        "add": add(a, b),
        "sub": sub(a, b),
        "mult": mult(a, b),
        "div": div(a, b)
    }

    return f"{math[oper]}"
