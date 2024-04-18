import os
from fpdf import FPDF
from .extract_data import import_from_json
from .formation import Formation


class FormationPDF(FPDF):
    def __init__(self, formation: Formation):
        super().__init__()
        self.formation = formation

    def header(self):
        self.set_fill_color(3, 16, 58)
        self.rect(0, 0, self.w, self.h, "F")

    def footer(self):
        w = 40
        self.image(
            os.path.abspath(
                "ressources/images/CHARTE_GRAPHIQUE_FORMAFOOT_24020740-removebg-preview.png"
            ),
            x=(self.w - w) / 2,
            y=self.h - 22.5,
            w=w,
        )
        # Définir la police et la taille du texte
        self.set_font("Graebenbach-RegularItalic", "I", 8)
        # Positionner le texte au-dessus de l'image
        self.set_y(self.h - 10)
        # Ajouter le numéro de page
        self.cell(0, 0, f"{self.page_no()}", align="C")

    def set_params(self):
        self.set_draw_color(255, 255, 255)

    def add_title(self):
        self.set_font("Graebenbach-Bold", "B", 24)
        self.set_text_color(255, 255, 255)
        self.set_y(40)
        self.set_x(40)
        self.multi_cell(150, 10, self.formation.titre, align="L", border=1)

    def add_top_left_angle(self):
        self.set_fill_color(98, 255, 124)
        self.rect(20, 20, 8, 70, "F")
        self.rect(20, 20, 50, 8, "F")

    def add_bottom_right_angle(self):
        self.set_fill_color(98, 255, 124)
        self.rect(self.w - 20, self.h - 20, -8, -70, "F")
        self.rect(self.w - 20, self.h - 20, -50, -8, "F")

    def add_formafoot(self):
        self.set_font("Graebenbach-Bold", "B", 12)
        self.set_y(-50)
        self.set_x(-80)
        self.cell(50, h=10, text="FORMAFOOT", align="R", border=1)

    def add_createur(self):
        self.set_font("Graebenbach-Bold", "B", 12)
        self.set_y(-40)
        self.set_x(-80)
        self.cell(50, h=10, text=self.formation.createur, align="R", border=1)

    def add_logo(self, image):
        image_width = 250
        image_height = 150

        x_position = (self.w - image_width) / 2
        y_position = (self.h - image_height) / 2

        self.image(
            image,
            x=x_position,
            y=y_position,
            w=image_width,
            h=image_height,
        )

    def add_prix(self):
        self.set_y(100)
        self.set_x(-70)
        self.cell(50, h=10, text=f"Prix: {self.formation.prix}", align="R", border=1)

    def add_prerequis(self):
        pr = self.formation.prerequis.replace(", ", "\n")
        self.set_y(50)
        self.set_x(50)
        self.multi_cell(50, h=10, text=f"Prerequis: {pr}", align="L", border=1)

    def add_financable(self):
        txt = "Oui" if self.formation.financable else "Non"
        self.set_y(110)
        self.set_x(20)
        self.cell(65, h=10, text=f"Finançable: {txt}", align="L", border=1)

    def add_apports(self):
        ap = self.formation.apports.replace(", ", "\n")
        self.set_y(110)
        self.set_x(110)
        self.multi_cell(50, h=10, text=f"Apports: {ap}", align="L", border=1)

    def add_duree_totale(self):

        self.set_y(100)
        self.set_x(20)
        self.cell(
            95, h=10, text=f"Duree totale: {self.formation.duree}", align="L", border=1
        )

    def add_doc_types(self):
        init_y = 180
        for doc_type, nb in self.formation.documents_types.items():
            self.set_y(init_y)
            self.set_x(50)
            self.cell(
                50,
                h=10,
                text=f"{doc_type}: {str(nb)}",
                align="L",
                border=1,
            )
            init_y += 10

    def title_section(self, y: int, text: str):
        self.set_font("Graebenbach-Regular", "", 20)
        self.set_y(y)
        self.set_x(20)
        self.set_text_color(3, 16, 58)
        self.set_fill_color(98, 255, 124)
        self.cell(self.w - 40, 10, text, 10, fill=True)
        self.set_text_color(255, 255, 255)
        self.set_font("Graebenbach-Regular", "", 12)

    def make_pdf(self):
        # Page 1
        self.add_page()
        self.add_font(
            "Graebenbach-Bold",
            "B",
            "/Users/remibareille/Library/Mobile Documents/com~apple~CloudDocs/Documents/Cours/FORMAFOOT/ressources/fonts/Graebenbach-Bold.otf",
        )
        self.add_font(
            "Graebenbach-Medium",
            "",
            "/Users/remibareille/Library/Mobile Documents/com~apple~CloudDocs/Documents/Cours/FORMAFOOT/ressources/fonts/Graebenbach-Medium.otf",
        )
        self.add_font(
            "Graebenbach-Regular",
            "",
            "/Users/remibareille/Library/Mobile Documents/com~apple~CloudDocs/Documents/Cours/FORMAFOOT/ressources/fonts/Graebenbach-Regular.otf",
        )
        self.add_font(
            "Graebenbach-RegularItalic",
            "I",
            "/Users/remibareille/Library/Mobile Documents/com~apple~CloudDocs/Documents/Cours/FORMAFOOT/ressources/fonts/Graebenbach-RegularItalic.otf",
        )
        self.set_params()
        self.add_logo(
            "/Users/remibareille/Library/Mobile Documents/com~apple~CloudDocs/Documents/Cours/FORMAFOOT/ressources/images/CHARTE GRAPHIQUE_FORMAFOOT_24020735.jpg"
        )

        self.add_top_left_angle()
        self.add_bottom_right_angle()
        self.add_title()
        self.add_formafoot()
        self.add_createur()

        # Page 2
        self.set_font("Graebenbach-Regular", "", 12)
        self.add_page()
        self.title_section(y=20, text="Informations")
        self.add_doc_types()
        self.add_prix()
        self.add_prerequis()
        self.add_financable()
        self.add_apports()
        self.add_duree_totale()

        # Page 3
        self.add_page()
        self.title_section(y=20, text="Contenu de la formation")

        x_module = 20
        x_chapitres = 40
        x_subchapitres = 60
        y = 40
        for module in self.formation.module:
            if y > 250:
                y = 40
                self.add_page()
            self.set_font("Graebenbach-Regular", "", 20)
            self.set_xy(x_module, y)
            self.cell(self.w, 10, module.titre)
            y += 15
            for chapitre in module.chapitres:
                if y > 250:
                    y = 40
                    self.add_page()
                self.set_font("Graebenbach-Regular", "", 18)
                self.set_xy(x_chapitres, y)
                print("chap", self.get_x())
                self.cell(self.w, 10, chapitre.chapitre_titre)
                y += 10
                for subchapitre in chapitre.subchapitres:
                    if y > 250:
                        y = 40
                        self.add_page()
                    self.set_font("Graebenbach-Regular", "", 16)
                    self.set_xy(x_subchapitres, y)
                    print("sub", self.get_x())
                    self.cell(self.w, 10, subchapitre.subchapitre_titre)
                    y += 10
            y += 10

        # Enregistrer le PDF
        pdf_output = "formation_info.pdf"
        self.output(pdf_output)
