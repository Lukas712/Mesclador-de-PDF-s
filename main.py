from PyPDF2 import PdfWriter
import os

merge = PdfWriter()
archive = os.listdir("arquivos")
print(archive)

for pdf in archive:
    if ".pdf" in pdf:
        merge.append(f"arquivos/{pdf}")

merge.write("Arquivos-Juntos.pdf")
merge.close()

