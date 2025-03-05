import faiss
import json 
import numpy as np
from sentence_transformers import SentenceTransformer 
from operations import combine_retrview_chunks,generate_query_embedding, retrieve_top_k_chunks
import cohere
from together import Together

client = Together(api_key="1274ae0e9cb88b078956f7f308d17e3a1728312e9abdd04396646cfcdfd2441f")

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


def generate_response_with_llam2(context, query):
    # Combine the context with the user's query for the input prompt
#     prompt = f"""Provide the accurate and detailed information to the user query. Here is some relevant information from the documents:\n{context}\n\nBased on this information, answer the following question:\n{query}
# """
#     prompt = f"""
# # You are an assistant that ensures **all relevant points are included** in the response.  
# # Below is the extracted information from documents related to the user's question:

# # {context}

# # Based on this information, answer the following question:  
# # {query}

# # ### Instructions:
# # - **Ensure that all distinct points mentioned in the provided information are listed.**
# # - **Do not omit any points** that are present in the extracted text.
# # - **It is not necessary to include all details**, but the response must contain all unique points.
# # - Keep the response structured and organized.
# # """
    
    prompt= f"""
 You are an assistant that ensures **all relevant points are included** in the response.
Below is the relevant information from the documents:
{context}
Based on this information, answer the following question:
{query}
Instructions:
Ensure all unique points are included—do not omit any relevant details.
Avoid unnecessary repetition, but make sure every distinct point is captured.
It is not necessary to include all details, but the response must contain all unique points."""

    response=client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    # model="mistralai/Mixtral-8x7B-v0.1",
    messages=[{"role": "user", "content": prompt, "max_tokens":2040,"temperature":0.7}],
    )
    return response.choices[0].message.content

# response = generate_response_with_cohere(top_k_context, query)
# print("Generated Response:\n", response)


# import faiss
# import json
# import torch
# import numpy as np
# from transformers import LlamaForCausalLM, LlamaTokenizer
# from sentence_transformers import SentenceTransformer 
# from operations import combine_retrview_chunks, generate_query_embedding, retrieve_top_k_chunks
# from transformers import AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf", use_auth_token=True)

# print("downloaded")
# # Load LLaMA 2 model and tokenizer
# MODEL_NAME = "meta-llama/Llama-2-7b-chat-hf"  # Choose a smaller model if needed
# tokenizer = LlamaTokenizer.from_pretrained(MODEL_NAME)
# model = LlamaForCausalLM.from_pretrained(MODEL_NAME, torch_dtype=torch.float32, device_map="cpu")

# def generate_response_with_llama(context, query):
#     """Generates a response using LLaMA 2 on CPU"""
#     prompt = f"Provide an accurate and detailed response to the query.\n\nContext:\n{context}\n\nQuestion:\n{query}\n\nAnswer:"

#     # Tokenize input
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024).to("cpu")

#     # Generate output
#     with torch.no_grad():
#         output = model.generate(
#             **inputs,
#             max_length=500,
#             temperature=0.7,
#             do_sample=True
#         )

#     # Decode response
#     response = tokenizer.decode(output[0], skip_special_tokens=True)
#     return response

# Example usage:
# query = "What is Thermal Insulation?"
# query_embedding = generate_query_embedding(query)
# distances, indices = retrieve_top_k_chunks(query_embedding, k=3)
# top_k_context = combine_retrview_chunks(indices=indices, metadata=metadata, k=3)
# response = generate_response_with_llama(top_k_context, query)
# print("Generated Response:\n", response)
