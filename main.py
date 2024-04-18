from pdf.formation import Formation
from pdf.pdf_formation import FormationPDF, import_from_json
import os


data = import_from_json(os.path.abspath("ressources/api object/api.json"))

formation = Formation(data=data)
print(formation)
pdf = FormationPDF(formation=formation)
pdf.make_pdf()
