from flask import Flask
from flask_mysqldb import MySQL
from config import config
from SMS.GET import listas_cursos, leer_curso
from SMS.POST import registar_curso
from SMS.PUT import actualizar_curso
from SMS.DELETE import eliminar_curso

app = Flask(__name__)

app.route('/cursos', methods=['GET'])(listas_cursos)
app.route('/cursos/<codigo>', methods=['GET'])(leer_curso)
app.route('/cursos', methods=['POST'])(registar_curso)
app.route('/cursos/<codigo>', methods=['PUT'])(actualizar_curso)
app.route('/cursos/<codigo>', methods=['DELETE'])(eliminar_curso)

def pagina_no_encontrada(error):
    return "PAGINA NO ENCONTRADA", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    conexion = MySQL(app)
    app.run()
