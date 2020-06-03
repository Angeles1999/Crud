from flask import Flask,jsonify,render_template,request,redirect
import pymysql
from ClaseConnect import *

app = Flask(__name__) #Hace referencia al objeto en el que estamos

@app.route("/") 
def presentacion():
    return render_template('inicio.html')

@app.route('/add',methods=["GET","POST"])
def add():
    try:
        Nombre=request.form.get("Nombre")
        Apellido=request.form.get("Apellido")
        cone=ClaseConnect()
        cone.EjecutarSQL("INSERT INTO participantes (Nombre,Apellido) VALUES('"+Nombre+"','"+Apellido+"')")
        cone.RealizarCambio()
        datos=cone.DevolverDatos()
        print (datos)
    except Exception:
        cone.NoRealizarCambio()
        print ("Error en las altas")
    return redirect("/all")

@app.route('/update',methods=["POST"])
def update():
    id=request.form.get('id')
    Nombre=request.form.get('Nombre')
    Apellido=request.form.get('Apellido')
    cone=ClaseConnect()
    cone.EjecutarSQL("UPDATE participantes SET Nombre='"+Nombre+"', Apellido='"+Apellido+"' WHERE id="+id)
    cone.RealizarCambio()
    return redirect("/all")

@app.route('/delete',methods=["GET","POST"])
def delete():
    try:     
        id=request.form.get('id')
        cone=ClaseConnect()
        cone.EjecutarSQL("DELETE FROM participantes WHERE id="+id)
        cone.RealizarCambio()
    except Exception:
        cone.NoRealizarCambio()
        print ("Error en las bajas")
    return redirect("/all")

@app.route("/list") 
def listadoalumnos():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM participantes")
    datos=cone.DevolverDatos()
    respuesta=jsonify(datos)
    cone.CerrarBaseDatos()
    return respuesta

@app.route("/view") 
def listview():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM participantes")
    data=cone.DevolverDatos()
    cone.CerrarBaseDatos()
    return render_template('listar.html',datos=data)

@app.route("/all") 
def listall():
    cone=ClaseConnect()
    cone.EjecutarSQL("SELECT * FROM participantes")
    data=cone.DevolverDatos()
    cone.CerrarBaseDatos()
    return render_template('add.html',datos=data)

if __name__ == "__main__": #__main__programa principal
    app.run()