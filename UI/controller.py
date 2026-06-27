import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDDGenre(self):
        genre= self._model.getAllGenre()
        for g in genre:
            self._view._ddGenre.options.append(ft.dropdown.Option(text=g))

    def fillDDCountry(self):
        country = self._model.getAllCountries()
        for c in country:
            self._view._ddCountry.options.append(ft.dropdown.Option(text=c))



    def handleCreaGrafo(self, e):
        genere = self._view._ddGenre.value
        country = self._view._ddCountry.value

        if genere is None or country is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Selezionare prima un genere e un country!", color="red")
            )
            self._view.update_page()
            return

        try:
            valore = int(self._view._txtMinSpesa.value)
        except ValueError:
            self._view.create_alert("Inserisci un numero intero valido")
            return

        if valore <= 0:
            self._view.create_alert("Il valore deve essere positivo")
            return

        self._model.creaGrafo(genere, country, valore)

        n, m = self._model.getGraphDetails()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! "
                    f"Il grafo è costituito di {n} nodi e {m} archi", color="green")
        )

        num, comp_max = self._model.getInfoComponenti()
        self._view.txt_result.controls.append(
            ft.Text(f"Numero componenti: {num}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Componente maggiore: {len(comp_max)} nodi")
        )
        if self._model.getGraphDetails()[0] == 0:
            self._view.create_alert("Crea prima il grafo")
            return
        top = self._model.getTopKArchi(k=5, massimo=True)
        self._view.txt_result.controls.append(ft.Text("Top 5 archi per peso:"))
        for u, v, peso in top:
            self._view.txt_result.controls.append(
                ft.Text(f"{u} -> {v} | peso: {peso}"))

        self._view.update_page()

    def handleAnalizzaArtista(self, e):
        pass

    def handleTrovaPercorso(self, e):
        pass
