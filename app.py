from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL
import requests as apirest
import sqlite3

dbconexion  = sqlite3.connect("tiendadb.db",check_same_thread=False)

dbcursor =dbconexion.cursor()

dbcursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
                 idUsuario INT UNSINGED AUTO_INCREMENT PRIMARY KEY,
                 nombre VARCHAR(10) not null,
                 edad INT not null
                 )""")

dbconexion.commit()



app = Flask(__name__)

#conexion db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'localhost'
app.config['MYSQL_PASSWORD'] = 'localhost'
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)


@app.context_processor
def date_now():
    return {
        'now':datetime.now().utcnow()
    }

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index/index.html')

@app.route('/usuario')
@app.route('/usuario/<string:nombre>')
@app.route('/usuario/<string:nombre>/<int:edad>')
def usuariodashboard(nombre='Invitado',edad=1):  # put application's code here

   if not edad=="" and not nombre=="":
        #return f'Hello World! {nombre} edad  {edad}'
        return render_template('usuario/usuario.html',nombre=nombre,edad=edad)
        #f'Hello World! {nombre} edad  {edad}'
   else:
       #return f'Hello World! {nombre}'
       return render_template('usuario/usuario.html', nombre=nombre)

@app.route('/consulta')
def consulta():

    result = apirest.get('https://api.breakingbadquotes.xyz/v1/quotes').json()
    print(result[0]['quote'])

    return render_template('consulta/consulta.html',quote=result[0]['quote'],author=result[0]['author'])


@app.route('/crear_usuario',methods=['POST','GET'])
def crear_usuario():

    if request.method == 'POST':
        usuario_name = request.form['usuario_name']
        edad_name = request.form['usuario_age']


        query = "INSERT INTO usuario values(null,?,?)"
        data = (usuario_name,edad_name)

        dbcursor.execute(query,data)
        dbconexion.commit()

        dbconexion.close()

        return redirect(url_for('usuariodashboard',nombre=usuario_name,edad=edad_name))
    else:
        return render_template('crear_usuario/form.html')

if __name__ == '__main__':
    app.run(debug=True)
