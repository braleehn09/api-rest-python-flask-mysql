from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

def registar_curso():    
    try:
       cursor=conexion.connection.cursor()
       sql= """INSERT INTO cursos (codigo, nombre, clase) 
                       VALUES ('{0}', '{1}', '{2}')""".format(request.json['codigo'], 
                                       request.json['nombre'], request.json['clase'])
       cursor.execute(sql)
       conexion.connection.commit()
       return jsonify({'mensaje':"curso registrado."}), 200
    except Exception as ex:
       return jsonify({'mensaje':"NOT CONEXION"}), 504

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

