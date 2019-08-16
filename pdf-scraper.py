import PyPDF2 as pypdf
pdfFile = open('/Users/abhijit/Desktop/code-for-boston/clean-slate/data/Archive/test1.pdf','rb')
pdfReader = pypdf.PdfFileReader(pdfFile)
numpages = pdfReader.numPages
for i in range(numpages):
    pageObj = pdfReader.getPage(i)
    a = pageObj.extractText()
    file1 = open("myfile.txt", "a")  # append mode
    file1.write(a)
    file1.close()