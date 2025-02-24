from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings_hf():
    chunks=[]
    with open("chunks_of_english_document_updated.txt",  'r', encoding='utf-8') as f:
        pdf_text=f.read()
        chunks=pdf_text.split("\n")
    print(f"total number of chunks:{len(chunks)}")
    return model.encode(chunks)

# chunks=[]
# with open("chunks_of_unit_operations.txt")
chunk_embeddings = generate_embeddings_hf()
print(f"Generated {len(chunk_embeddings)} embeddings")


# Convert embeddings to a numpy array
embedding_matrix = np.array(chunk_embeddings).astype('float32')

print(embedding_matrix[20])
# Create an FAISS index
index = faiss.IndexFlatL2(embedding_matrix.shape[1])  # L2 similarity
print(f"index:{index}")
index.add(embedding_matrix)  # Add embeddings to the index

# Save index for future use
faiss.write_index(index, "embeddings_index.faiss")
print(f"Stored {index.ntotal} embeddings in FAISS index")
