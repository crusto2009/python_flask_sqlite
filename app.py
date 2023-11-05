from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
from flask_mysqldb import MySQL
from routers import init_app

app = Flask(__name__)
app.secret_key ="#$#ASFSD"

#conexion dbconexion
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

init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
