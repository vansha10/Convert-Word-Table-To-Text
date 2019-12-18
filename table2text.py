from docx import Document

wordDoc = Document('table.docx')

document = Document()

for table in wordDoc.tables:
    for row in table.rows:
        s = ""
        for cell in row.cells:
            s += cell.text + " - "
        document.add_paragraph(s)
        
document.save("text.docx")