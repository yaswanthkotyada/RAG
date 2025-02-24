import json


chunks=[]
with open("chunks_of_english_document_updated.txt",  'r', encoding='utf-8') as f:
    pdf_text=f.read()
    chunks=pdf_text.split("\n")

metadata = [{"chunk_id": i, "text": chunk, "source": "scholarship_document_for_sc_students.pdf"} for i, chunk in enumerate(chunks)]


# Save metadata to a JSON file
with open("metadata.json", "w") as f:
    json.dump(metadata, f)
