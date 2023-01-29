from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

def listas_cursos():
    try:
        # Validar que la conexión a la base de datos esté activa
        if conexion.connection.open == False:
            return jsonify({'mensaje':"Error en la conexión a la base de datos"}), 500
        cursor=conexion.connection.cursor()
        sql="SELECT * FROM cursos"
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursos=[]
        for me in datos:
            curso = {
             'codigo':me[0],
             'nombre':me[1],
             'clase':me[2]
            }
            cursos.append(curso)
        return jsonify({'cursos':cursos,'mensaje':"cursos listados."}), 200
    except Exception as ex:
        return jsonify({'mensaje':"Error"})

def leer_curso(codigo):
    try:
        # Validar que se haya proporcionado un código
        if codigo is None:
            return jsonify({'mensaje':"Debe proporcionar un código de curso"}), 400
        # Validar que la conexión a la base de datos esté activa
        if conexion.connection.open == False:
            return jsonify({'mensaje':"Error en la conexión a la base de datos"}), 500
        cursor=conexion.connection.cursor()
        sql="SELECT codigo, nombre, clase FROM cursos WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            curso={'codigo': datos[0],
                   'nombre': datos[1],
                   'clase': datos[2]}

            return jsonify({'cursos':curso,'mensaje':"curso encontrado."}), 200
        else:
            return jsonify({'mensaje':"curso no encontrado."}), 404
    except Exception as ex:
            return jsonify({'mensaje':"Error"})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

