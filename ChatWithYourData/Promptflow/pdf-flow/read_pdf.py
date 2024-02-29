from promptflow import tool
import PyPDF2

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool
def read_pdf(input1: str) -> str:
  pdf = open(input1, 'rb')
  pdfReader = PyPDF2.PdfReader(pdf)
  pageObj = pdfReader.pages[0]
  content = pageObj.extract_text()
  pdf.close()
  return content
