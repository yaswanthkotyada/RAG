import pdfplumber

pdf_text =""
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text=""
        for page in pdf.pages:
            text+=page.extract_text()
        with open("chunks_ext_txt.txt", "w", encoding="utf-8") as f:
                f.write(text )           
    return text

pdf_text =extract_text_from_pdf("english_document_updated.pdf")
print(pdf_text[3])

def chunking_txt_to_paragphs(text):
    try:
        paragphs=text.split("\n")
        chunks= [para.strip() for para in paragphs if para.strip()]
        with open("chunks_of_english_document_updated.txt", "w", encoding="utf-8") as f:
            for chunk in chunks:
                f.write(chunk + "\n")
        return chunks
    except Exception as e:
        print(f"excpetion:{e}")
        return e
chunks =chunking_txt_to_paragphs(pdf_text)
print(f"total number of chunks:{len(chunks)}")
print(f"the first two chunks are:{chunks[:2]}")

