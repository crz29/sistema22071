from colorama import Cursor
from flask import Flask
from flask import render_template

#5. escribimos
from flaskext.mysql import MySQL



app= Flask(__name__)
#2.Defino acá "app" (aplicacion del tipo Flask)
#esto se ejecuta con app.run
#aaa
#4.escribimos estas 6 lineas, siempre son las mismas en MySql.
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost' #porque está en nuestra PC
app.config['MYSQL_DATABASE_USER']= 'root' #root es el usuario por defecto
app.config['MYSQL_DATABASE_PASSWORD']= '' #la password es vacía, no tiene
app.config['MYSQL_DATABASE_DB']= 'sistema22071' #se coloca el nombre que le pusimos en el sistema(phpmyadmin)

mysql.init_app(app) #mysql va abajo


#3.le doy la ruta a la que me redirije
@app.route("/") #antes de ir a la vista, viene acá (abre la conexión a la BD)y luego retorna la vista.
# Cómo escribirlo: solo se escribe @ap y enter (se elige "app route decorator")
def index():
    #6. ahora creamos un objeto SQL con la sentencia adentro para insertar el registro creado en phpmyadmin
    sql="INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'valeria', 'vale11@genial.com', 'folatoa.jpg');"
    
    conn=mysql.connect() #7. abro una conexion con la BD (el mysql de arriba)
    #conn es un objeto que creo a partir de mysql
    cursor=conn.cursor() #8. creo un cursor a partir de la conexión
    cursor.execute(sql)#9 al cursor le meto la sentencia sql
    conn.commit()

    return render_template('empleados/index.html')#retorna una vista (index.html), NO datos

@app.route("/juanca")
def juancito():
    return render_template('empleados/juanca.html')


if __name__ == '__main__': 
#1.este es el punto de entrada a la aplicación que llama a app.run
    app.run(debug=True)