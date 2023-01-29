from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

def actualizar_curso(codigo):
    try:
        # Validar que se haya proporcionado un código
        if codigo is None:
            return jsonify({'mensaje':"Debe proporcionar un código de curso"}), 400
        
        # Validar que se hayan proporcionado los datos necesarios para actualizar el curso
        if 'nombre' not in request.json or 'clase' not in request.json:
            return jsonify({'mensaje':"Debe proporcionar el nombre y clase del curso"}), 400
        
        # Validar que la conexión a la base de datos esté activa
        if conexion.connection.open == False:
            return jsonify({'mensaje':"Error en la conexión a la base de datos"}), 500

        cursor=conexion.connection.cursor()
        sql= """UPDATE cursos SET nombre = '{0}', clase = '{1}'
                        WHERE codigo = '{2}'""".format(request.json['nombre'], 
                                                 request.json['clase'],codigo)
        cursor.execute(sql)
        conexion.connection.commit()

        return jsonify({'mensaje':"curso actualizado."}), 200
    except Exception as ex:
        return jsonify({'mensaje':"Error"}), 504

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()