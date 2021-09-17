import PyPDF2

merger = PyPDF2.PdfFileMerger()
files = ['Python_Tutorial.pdf', 'Python_Tutorial_rotated.pdf']

for pdf_file in files:
    with open(pdf_file, 'rb') as file:
        pdf_merger.append(file)

with open('out.pdf', 'wb') as pdf_file_merged:
    pdf_merger.write(pdf_file_merged)
