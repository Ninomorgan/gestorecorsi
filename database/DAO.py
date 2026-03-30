from database.DB_connect import DBConnect
from model.corso import Corso


class DAO():

    @staticmethod
    def getCodins():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query="""select codins
                from corso 
               """
        cursor.execute(query)
        res=[]
        for row in cursor:
            res.append(Corso(
                codins=row["codins"],
                nome=row["nome"],
                crediti=row["crediti"],
                pd=row["pd"],

            ))

        cursor.close()
        cnx.close()
        return res