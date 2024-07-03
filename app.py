from bot import chat
import aspose.pdf as pdf

input = pdf.Document("C://Users//Somya Sharma//OneDrive//Desktop//Learning//projects//python_projects//PDF_reader//SQL INTERVIEW QUESTIONS.pdf")
txt = pdf.text.TextAbsorber()
txt.visit(input.pages[1])
pdf_text = txt.text
prompt = f"Act as an assitant and answer what is SQL ? based on the given data. data = {pdf_text}"

responce = chat(prompt)
print(responce)



