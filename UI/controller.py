import flet as ft

from model.model import Model


class Controller:
    def __init__(self, view):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = Model()
        self._ddCodinsValue = None

    def handlePrintCorsiPD(self,e):
        self._view.txt_result.controls.clear()
        pd= self._view.doPD.value

        if pd is None:
            (self._view.create_alert ("Attenzione seleziona periodo didattico"))
            self._view.update_page()
            return

        if pd == "I":
            pdInt=1
        else: pdInt=2

        corsiPD= self._model.getCorsiPD(pdInt)

        if not len(corsiPD):
            self._view.tct_result.controls.append( ft.Text(f"Nessun corsdo trovato per {pd} periodo"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Ecco i corsi del {pd} periodo didattico"))

        for c in corsiPD:
            self._view.txt_result.controls.append(ft.Text(c))
        self._view.update_page()






    def handlePrintIscrittiCorsiPD(self, e):
        self._view.txt_result.controls.clear()
        pd = self._view.doPD.value

        if pd is None:
            (self._view.create_alert("Attenzione seleziona periodo didattico"))
            self._view.update_page()
            return

        if pd == "I":
            pdInt = 1
        else:
            pdInt = 2

        corsi = self._model.getCorsiPDwIscritti(pdInt)

        if not len(corsi):
            self._view.tct_result.controls.append(ft.Text(f"Nessun corsdo trovato per {pd} periodo"))
            self._view.update_page()
            return
        self._view.txt_result.controls.append(ft.Text(f"Ecco i corsi del {pd} periodo didattico con dettaglio iscritti"))

        for c in corsi:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]} -- N iscritti: {c[1]}")
            )
        self._view.update_page()

    def handlePrintIscrittiCodins(self,e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
            self._view.create_alert("Selezionare un insegnamento")
            self._view.update_page()
            return

        studenti = self._model.getStudentiCorso(self._ddCodinsValue.codins)

        if not len(studenti):
            self._view.txt_result.controls.append(
                ft.Text("NESSUNO STUDENTE ISCIRTTO AL CORSO")
            )
            self._view.update_page()
            return
        self._view.txt_result.controls.append(
            ft.Text(f"ecco gli studenti isciritti al corso {self._ddCodinsValue}")
        )

        for s in studenti:
            self._view.txt_result.controls.append(
                ft.Text(s)
            )
            self._view.update_page()

    def handlePrintCDSCodins(self, e):
        self._view.txt_result.controls.clear()
        if self._ddCodinsValue is None:
                self._view.create_alert("Selezionare un insegnamento")
                self._view.update_page()
                return

        cds= self._model.getCDSofCorso(self._ddCodinsValue.codins)
        #lista tuole

        if not len(cds):
            self._view.txt_result.controls.append(ft.Text(f"Nessun cds afferente al corso {self._ddCodinsValue}"))
            self._view.update_page()
            return

        self._view.txt_result.controls.append(
            ft.Text(f"Di seguito i cds che frequentano il orso {self._ddCodinsValue}"))
        for c in cds:
            self._view.txt_result.controls.append(
                ft.Text(f"{c[0]}- n. iscritti: {c[1]}")
            )
            self._view.update_page()



    def fillddCodins(self): #lo prendiamo dal modello
        #for cod in self._model.getCodins():
        #    self._view.ddCodins.append(
        #        ft.dropdown.Option(cod)
        #    )
        #pass
        for c in self._model.getAllCorsi():
            self._view.doCodins.options.append(ft.dropdown.Option(
                key=c.codins,
                data=c,
                on_click=self._choiceDOCodins
            ))
            pass

    def _choiceDOCodins(self,e):
        self._ddCodinsValue= e.control.data
        print(self._ddCodinsValue)