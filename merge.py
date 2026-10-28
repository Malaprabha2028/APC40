from pypdf import PdfReader, PdfWriter

writer = PdfWriter()

for file in ["1st.pdf", "2nd.pdf", "3rd.pdf"]:
    reader = PdfReader(file)

    for page in reader.pages:
        writer.add_page(page)

with open("pdf_merg.pdf", "wb") as output:
    writer.write(output)

print("PDFs merged successfully!")