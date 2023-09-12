import PyPDF2

pdfiles = ["sample1.pdf","sample2.pdf","sample3.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdfiles:
    pdFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)
pdFile.close()
merger.write('merged.pdf')


