from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    def getCodins(self):
        return DAO.getCodins()

    def getAllCorsi(self):
        return DAO.getCAllCorsi()

    def getCorsiPD(self, pd):
        return DAO.getCorsiPD(pd)

    #SE DOBBIAMO AGGIUNGERE UN METODO PRE PRINTARLI ORDINATI LO FACCIMAO NEL MODEL
    def getCorsiPDwIscritti(self, pd):
        result=DAO.getCorsiPDwIscritti(pd)
        result.sort(key = lambda s: s[1], reverse=True) #ordinata per numero iscritit
        return result

    def getStudentiCorso(self, codins):
        studenti =DAO.getStudentiCorso(codins)
        studenti.sort(key = lambda s: s.cognome)
        return studenti

    def getCDSofCorso(self, codins):
        cds= DAO.getCDSofCorso(codins)
        cds.sort(key = lambda x: x[1], reverse=True)  #ordinati per corso
        return cds
