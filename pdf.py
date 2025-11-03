from pypdf import PdfReader
pdf = PdfReader('ASISTENCIA.pdf')
num_paginas = len(pdf.pages)
print(num_paginas)
pagina = pdf.pages[0]
print(pagina.extract_text(0))
