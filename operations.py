import faiss
import json 
import numpy as np
from sentence_transformers import SentenceTransformer 

index=faiss.read_index("embeddings_index.faiss")

print(f"Loaded {index.ntotal} embeddings from the FAISS index.")

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_query_embedding(query):
    # Generate an embedding for the user's query
    return np.array(model.encode([query])).astype('float32')

# Example query
def retrieve_top_k_chunks(query_embedding, k=3):
    # Perform the similarity search in FAISS
    distances, indices = index.search(query_embedding, k)  # k is the number of results to return
    return distances, indices

# Perform similarity search to get the top 3 chunks


def combine_retrview_chunks(indices, metadata, k=10):
    try:
        context=""
        for i in range (k) :
            chunk_idx=indices[0][i]
            chunk_text=metadata[chunk_idx]["text"]
            context+=chunk_text+"\n\n"
        return context
    except Exception as e:
        print(f"exception:{e}")
        return e
    

            
            


