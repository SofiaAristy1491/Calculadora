from flask import Flask, request, render_template
from operaciones import sumar 
from operaciones import resta
from operaciones import multiplicacion
from operaciones import division
from operaciones import division2
from livereload import Server


app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
# '''
# <h1> Aplicación de la Calculadora</h1>
# <a href="/suma?num1=5&num2=4"> Ir a la página de suma</a> 
# <a href="/resta?num1=5&num2=4"> Ir a la página de resta</a> 
# <a href="/multiplicacion?num1=5&num2=4"> Ir a la página de multiplicacion</a> 
# <a href="/division?num1=5&num2=4"> Ir a la página de division</a> 
# <a href="/division piso?num1=5&num2=4"> Ir a la página de division piso</a> 


@app.route("/suma")
def ruta_suma():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None: 
        return "faltan datos"
    return f"la suma num1 y num2 es {sumar(num1,num2)}"

@app.route("/resta")
def ruta_resta():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None: 
        return "faltan datos"
    return f"la suma num1 y num2 es {resta(num1,num2)}"

@app.route("/multiplicacion")
def ruta_multiplicacion():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None: 
        return "faltan datos"
    return f"la suma num1 y num2 es {multiplicacion(num1,num2)}"

@app.route("/division")
def ruta_division():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None: 
        return "faltan datos"
    return f"la suma num1 y num2 es {division(num1,num2)}"

@app.route("/division piso")
def ruta_division2():
    num1=request.args.get("num1",type=float)
    num2=request.args.get("num2",type=float)
    if num1 is None or num2 is None: 
        return "faltan datos"
    return f"la division piso num1 y num2 es {division2(num1,num2)}"

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve()
