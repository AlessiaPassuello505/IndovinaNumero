from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def get_numeroMassimo(self):
        return self._model._nMax


    def get_numeroTentativiMax(self):
        return self._model._tMax


    def get_numeroTentativi(self):
        return self._model._t


    def reset(self,e):
        self._model.reset()
        self._view._txtT.value=self._model._t
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Indovina quale numero sto pensando"))
        self._view.update()

    def play(self,e):
        tnt_str=self._view._txtInterattivo.value
        try:
            tnt=int(tnt_str)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Errore: devi inserire un numero"))
            self._view.update()
            return

        res=self._model.play(tnt)
        if res==0:
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto! Il valore corretto era: {tnt},color=green"))

        elif res==2:
            self._view._lvOut.controls.append(ft.Text(f"Hai perso! Il valore corretto era: {self._model._segreto}"))
            self._view.update()

        elif res==-1:
            self._view._lvOut.controls.append(ft.Text(f"Riprovare! Il segreto è più piccolo di {tnt}"))
            self._view.update()

        else:
            self._view._lvOut.controls.append(ft.Text(f"Riprovare! il segreto è più grende di {tnt}"))
            self._view.update()


