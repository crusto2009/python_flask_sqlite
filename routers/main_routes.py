from flask import Blueprint,render_template,redirect,url_for,request,flash
import requests as apirest
from dbconexion import ConexionDB

main_bp = Blueprint('api',__name__)



@main_bp.route('/')
def hello_world():  # put application's code here
    return render_template('index/index.html')


@main_bp.route('/listar_usuarios')
def listar_usuarios():
    db = ConexionDB()

    usuarios = db.dbcursor.execute("SELECT idUsuario,nombre,edad FROM usuario")

    #db.execute_query()

    usuarios = db.dbcursor.fetchall()
    print("Usuarios",usuarios)

    return render_template('usuario/listar_usuarios.html', usuarios=usuarios)


@main_bp.route('/borrar_usuario/<string:id>')
def borrar_usuario(id):

    db = ConexionDB()
    db.deleteUsuario(id)
    flash("El usuario ha sido eliminado","success")
    return redirect(url_for('api.listar_usuarios'))


@main_bp.route('/usuario')
@main_bp.route('/usuario/<string:nombre>')
@main_bp.route('/usuario/<string:nombre>/<int:edad>')
def usuariodashboard(nombre='Invitado',edad=1):  # put application's code here

   if not edad=="" and not nombre=="":
        #return f'Hello World! {nombre} edad  {edad}'
        return render_template('usuario/usuario.html',nombre=nombre,edad=edad)
        #f'Hello World! {nombre} edad  {edad}'
   else:
       #return f'Hello World! {nombre}'
       return render_template('usuario/usuario.html', nombre=nombre)

@main_bp.route('/consulta')
def consulta():

    result = apirest.get('https://api.breakingbadquotes.xyz/v1/quotes').json()
    print(result[0]['quote'])

    return render_template('consulta/consulta.html',quote=result[0]['quote'],author=result[0]['author'])


@main_bp.route('/crear_usuario',methods=['POST','GET'])
def crear_usuario():

    if request.method == 'POST':
        usuario_name = request.form['usuario_name']
        edad_name = request.form['usuario_age']

        db = ConexionDB()
        db.save(usuario_name,edad_name)



        return redirect(url_for('api.usuariodashboard',nombre=usuario_name,edad=edad_name))
    else:
        return render_template('/crear_usuario/form.html')