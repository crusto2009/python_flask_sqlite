import sqlite3

class ConexionDB:

    dbconexion  = sqlite3.connect("tiendadb",check_same_thread=False)

    dbcursor =dbconexion.cursor()

    dbcursor.execute("""CREATE TABLE IF NOT EXISTS usuario(
                     idUsuario INTEGER PRIMARY KEY,
                     nombre VARCHAR(10) not null,
                     edad INTEGER not null
                     )""")

    dbconexion.commit()

    def save(self,usuario,edad):
        query = "INSERT INTO usuario values(null,?,?)"
        data = (usuario, edad)
        self.dbcursor.execute(query, data)
        self.dbconexion.commit()
        #self.closeConexion()

    def deleteUsuario(self,id):

        try:
            print(id)
            query = "DELETE FROM usuario WHERE idUsuario=?"
            self.dbcursor.execute(query,id)
            self.dbconexion.commit()
            #self.closeConexion()
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def execute_query(self, query):
        try:
            if self.dbconexion:
                self.dbcursor.execute(query)
                self.dbconexion.commit()
                print("Consulta ejecutada con éxito")
            else:
                print("No hay conexión establecida a la base de datos")
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def closeConexion(self):
        if self.dbconexion:
            self.dbconexion.close()
            print("Conexión cerrada")

    def getConexion(self):
        return self.dbconexion

    def getCursor(self):
        return self.dbcursor