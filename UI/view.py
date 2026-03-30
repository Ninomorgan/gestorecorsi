import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "GESTORE CORSI"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None

        #non obbligatorio
        # menu a tendina
        self.doPD = None
        self.doCodins=None
        #bottoni
        self.btnPrintCorsiPD=None
        self.btnPrintIscrittiCorsiPD=None
        self.btnPrintIscrittiCodins=None
        self.btnPrintCDSCodins=None


    def load_interface(self):
        # title
        self._title = ft.Text("Gestore Corsi - Edizione 2026", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW1
        self.doPD= ft.Dropdown(label="Periodo didattico",
                               options=[ft.dropdown.Option("I"), ft.dropdown.Option("II")], #opzioni primo e secondo periodo didattico
                             )

        self.btnPrintCorsiPD = ft.ElevatedButton(text="Stampa Corsi",
                                                on_click= self.controller.handlePrintCorsiPD)

        self.btnPrintIscrittiCorsiPD = ft.ElevatedButton(text="Stampa Corsi",
                                                on_click= self.controller.handlePrintIscrittiCorsiPD)

        row1= ft.Row([self.doPD,self.btnPrintCorsiPD , self.btnPrintIscrittiCorsiPD])

        #row2

        self.doCodins = ft.Dropdown(label="Corso", width=200) #gestito da controller, lo riempio là
        self._controller.fillddCodins()

        self.btnPrintIscrittiCodins = ft.ElevatedButton(text="Stampa Iscritti al corso",
                                                 on_click=self.controller.handlePrintIscrittiCodins,
                                                        width=300)

        self.btnPrintCDSCodins = ft.ElevatedButton(text="Stampa CDS afferenti",
                                                         on_click=self.controller.handlePrintCDSCodins)

        row2 = ft.Row([self.doPD,self.btnPrintIscrittiCodins,self.btnPrintCDSCodins])
        self._page.add(row1,row2)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
