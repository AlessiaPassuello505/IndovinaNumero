import flet
import flet as ft

class View(object):
    def __init__(self, page):    #crea la pagina
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txtNmax=ft.TextField(label="Numero Massimo", value=self._controller.get_numeroMassimo(),disabled=True)
        self._txtTmax=ft.TextField(label="Numero tentativi massimo", value=self._controller.get_numeroTentativiMax(),disabled=True)
        self._txtT=ft.TextField(label="Numero tentativi rimanenti",value=self._controller.get_numeroTentativi(),disabled=True)

        self._txtInterattivo=ft.TextField(label="Valore")
        self._btnreset=ft.ElevatedButton(text="Nuova partita",on_click=self._controller.reset)
        self._btngioca=ft.ElevatedButton(text="Indovina", on_click=self._controller.play)

        self._lvOut=ft.ListView(expand=True)  #voglio che sia scrollabile


        self._row1=ft.Row(controls=[self._txtNmax,self._btnreset])
        self._row2=ft.Row(controls=[self._txtT,self._txtTmax])
        self._row3=ft.Row(controls=[self._txtInterattivo,self._btngioca])
        self._page.add(self._row1,self._row2,self._row3,self._lvOut)

        self._page.update()          #aggiorna la mia pagina

    def setController(self,controller):
        self._controller = controller      #carica nella variabile interna della view il controller

    def update(self):
        self._page.update()