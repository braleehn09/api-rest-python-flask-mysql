from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
conexion = MySQL(app)

def eliminar_curso(codigo):    
    try:
       cursor=conexion.connection.cursor()
       sql= "DELETE FROM cursos WHERE codigo = '{0}'".format(codigo)
       cursor.execute(sql)
       conexion.connection.commit()
       print(sql)
       return jsonify({'mensaje':"curso eliminado."}), 200
    except Exception as ex:
       return jsonify({'mensaje':"NOT CONEXION"}), 504

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()