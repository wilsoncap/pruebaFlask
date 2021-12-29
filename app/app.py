from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

#conexion a MySQL
# app.config['MYSQL_HOST'] = 'db4free.net'
# app.config['MYSQL_USER'] = 'wilsonpru270921'
# app.config['MYSQL_PASSWORD'] = 'wili@159'
# app.config['MYSQL_DB'] = 'prueba270921'

# conexion = MySQL(app)

# @app.before_request
# def before_request():
#   print('Antes de la peticion....')

# @app.after_request
# def after_request(response):
#   print('Despues de la peticion')
#   return response


@app.route('/')
def principal():
  return "<h1>Hola soy la pagina principal</h1>"


@app.route('/colores')
def listar_cursos():
  data = {}

  try:
    cursor = conexion.connection.cursor()
    sql = 'SELECT id_color, nombre_color, referencia_color, categoria FROM colores ORDER BY nombre_color ASC'
    cursor.execute(sql)
    cursos = cursor.fetchall()
    print(cursos)
    data['cursos'] = cursos
    data['mensaje'] = 'Exitoso en la conexion'
  except Exception as ex:
    data['mensaje'] ='Error...'
  return jsonify(data)
  #return render_template('allcursos.html', data=data)



#@app.route('/mostrarcursos')
#def show_cursos():
  #cursos = get('http//127.0.0.1:5000/cursos').json()


# def pagina_no_encontrada(error):
#   # return render_template('404.html'), 404
#   return redirect(url_for('index'))


if __name__=='__main__':
  # app.add_url_rule('/query_string', view_func=query_string)# enlazar funcion hacia la url'query_string', no necesariamente tienen que tener el mismo nombre
  # app.register_error_handler(404, pagina_no_encontrada)
  app.run(debug=True, port=5000)






# py -m pip install virtualenv  --> para crear entorno virtual globalmente
# Virtualenv -p python3 env, otro_nombre  --> para crear entorno virtual localmente
# pip list -->para ver lo que hay en la ruta actual
# pip install flask --> para insalar flask
# .\env\Scripts\Activate --> para entrar al entorno virual donde podemos instalar paquetes, librerias y framework
# deactivate --> para salir del entorno virtual
# pip freeze > requirements.txt --> crea un archivo con todos los paquetes del proyecto para que se puedan migrar a otro proyecto
# pip install -r requirements.txt --> para instalar los paquetes en otro proyecto
# python .\app\app.py --> se ejecuta en el entorno virtual
# python.exe pip install --upgrade pip
# python .\app\app.py --> para levantar el servidor
# python .\src\app.py
# pip list --outdated --> para ver los paquetes que estan desactualizados
# pip show "nombre del paquete" --> para ver toda la informacion mas detallada del paquete
# pip check "nombre del paquete" --> sirve para ver si el paquete tiene algun faltante de otra dependencia o estas esten rotas
# pip install flask-sqlalchemy --> modulo para comunicarse con base de datos
# pip install flask-marshmallow --> modulo para definir squemas en nuestra base de datos
# pip install marshmallow-sqlalchemy --> librerias que trabajan entre ellas mismas
# pip install pymysql -->modulo para poder crear conexion con la base de datos