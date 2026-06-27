import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "TdP Chinook - Simulazione esame"
        self._page.horizontal_alignment = "CENTER"
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.window_height = 850
        self._page.window_width = 1100
        try:
            self._page.window_center()
        except Exception:
            pass

        # controller: initialized in main after Controller is created
        self._controller = None

        # graphical elements
        self._title = None
        self._subtitle = None

        # Punto 1
        self._ddGenre = None
        self._ddCountry = None
        self._txtMinSpesa = None
        self._btnCreaGrafo = None

        # Punto 2
        self._ddArtist = None
        self._txtK = None
        self._btnAnalizzaArtista = None
        self._btnTrovaPercorso = None

        # output
        self.txt_result = None

    def load_interface(self):
        # Title
        self._title = ft.Text(
            "Simulazione d'esame TdP - Database Chinook",
            color="blue",
            size=24,
            weight=ft.FontWeight.BOLD,
        )
        self._subtitle = ft.Text(
            "Struttura pronta: completa DAO, Model e Controller per risolvere la traccia.",
            size=14,
            italic=True,
        )
        self._page.controls.append(self._title)
        self._page.controls.append(self._subtitle)

        # -------------------------
        # Punto 1 - input grafo
        # -------------------------
        self._ddGenre = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona un genere",
            width=250,
        )

        self._ddCountry = ft.Dropdown(
            label="Paese cliente",
            hint_text="Seleziona un paese",
            width=250,
        )

        self._txtMinSpesa = ft.TextField(
            label="Spesa minima artista (€)",
            hint_text="es. 10",
            width=220,
        )

        self._btnCreaGrafo = ft.ElevatedButton(
            text="Crea grafo",
            on_click=self._controller.handleCreaGrafo,
        )

        # metodi volutamente lasciati da completare nel Controller
        self._controller.fillDDGenre()
        self._controller.fillDDCountry()

        row1 = ft.Row(
            [self._ddGenre, self._ddCountry, self._txtMinSpesa, self._btnCreaGrafo],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END,
            wrap=True,
        )
        self._page.controls.append(row1)

        # -------------------------
        # Punto 2 - analisi grafo
        # -------------------------
        self._ddArtist = ft.Dropdown(
            label="Artista nel grafo",
            hint_text="Seleziona un artista",
            width=320,
        )

        self._txtK = ft.TextField(
            label="K massimo",
            hint_text="es. 5",
            width=150,
        )

        self._btnAnalizzaArtista = ft.ElevatedButton(
            text="Analisi componente",
            on_click=self._controller.handleAnalizzaArtista,
        )

        self._btnTrovaPercorso = ft.ElevatedButton(
            text="Trova percorso migliore",
            on_click=self._controller.handleTrovaPercorso,
        )

        row2 = ft.Row(
            [self._ddArtist, self._txtK, self._btnAnalizzaArtista, self._btnTrovaPercorso],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.END,
            wrap=True,
        )
        self._page.controls.append(row2)

        # Result area
        self.txt_result = ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True,
        )
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
