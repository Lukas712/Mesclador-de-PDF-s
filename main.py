from PyPDF2 import PdfWriter
import os

merge = PdfWriter()
archive = os.listdir("/Users/Lukas/Vscode/Mesclador-de-PDF-s/arquivos")

for pdf in archive:
    merge.append(f"/Users/Lukas/Vscode/Mesclador-de-PDF-s/arquivos/{pdf}")

merge.write("Arquivos-Juntos.pdf")
merge.close()

