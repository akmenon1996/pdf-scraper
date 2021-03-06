import PyPDF2 as pypdf
import os

directory = '../test-pdfs'
for file in os.listdir(directory):
    if not file.endswith(".pdf"):
        continue
    with open(os.path.join(directory,file), 'rb') as pdfFile:  # Changes here
        pdfReader = pypdf.PdfFileReader(pdfFile)
        numpages = pdfReader.numPages
        for i in range(numpages):
            pageObj = pdfReader.getPage(i)
            a = pageObj.extractText()
            file1 = open(f"{file}.txt", "a")  # append mode
            file1.write(a)
            file1.close()