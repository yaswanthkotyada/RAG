import faiss
import json 
import numpy as np
from sentence_transformers import SentenceTransformer 
from operations import combine_retrview_chunks,generate_query_embedding, retrieve_top_k_chunks
import cohere


# with open("metadata.json","r") as f:
#     metadata=json.load(f)
    



# # Example query
# query = "What is Thermal Insulation ?"
# query_embedding = generate_query_embedding(query)




# # Perform similarity search to get the top 3 chunks
# distances, indices = retrieve_top_k_chunks(query_embedding, k=3)

# # Show the results
# # for i, idx in enumerate(indices[0]):
# #     print(f"Rank {i+1}:")
# #     print(f"Chunk Text: {metadata[idx]['text'][:300]}...")  # Preview of the chunk text
# #     print(f"Distance: {distances[0][i]}")
# #     print("-" * 40)


# top_k_context=combine_retrview_chunks(indices=indices, metadata=metadata, k=3)
# print("Combined Context:\n", top_k_context) 
        

# Set your Cohere API key
cohere_api_key = "4wSvi9EFIAb0qQ9MCow6gj4Y1su8VKFd6JD1oXIg"  # Replace with your actual Cohere API key

# Initialize Cohere client
co = cohere.Client(cohere_api_key)

def generate_response_with_cohere(context, query):
    # Combine the context with the user's query for the input prompt
    prompt = f"Provide the accurate and detailed information to the user query. Here is some relevant information from the documents:\n{context}\n\nBased on this information, answer the following question:\n{query}"

    # Use Cohere's generate API to get a response
    response = co.generate(
        model='command-xlarge',  # Use Cohere's largest model (adjust as necessary)
        prompt=prompt,
        max_tokens=500,  # Adjust the response length as needed
        temperature=0.7  # Controls the creativity of the response (higher = more creative)
    )

    return response.generations[0].text.strip()


# response = generate_response_with_cohere(top_k_context, query)
# print("Generated Response:\n", response)
