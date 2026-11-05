import pandas as pd
import gradio as gr
from sentence_transformers import SentenceTransformer, util
from transformers import pipeline
import torch

# 1. Load your dataset (Assumes 'df' is already loaded from your previous cell)
# If not, use: df = pd.read_csv("Harsh college_info_dataset_input_output.csv")
knowledge_base = df.dropna()

# 2. Initialize Models
# Semantic Search Model (for retrieval)
embedder = SentenceTransformer('all-MiniLM-L6-v2')
# Generative Model (for context-aware refinement)
generator = pipeline("text2text-generation", model="google/flan-t5-base")

# 3. Pre-calculate embeddings for the knowledge base
corpus_embeddings = embedder.encode(knowledge_base['input'].tolist(), convert_to_tensor=True)

def chatbot_response(user_query):
    # Step A: Retrieval (Find the most similar question in dataset)
    query_embedding = embedder.encode(user_query, convert_to_tensor=True)
    hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=1)
    
    best_hit = hits[0][0]
    score = best_hit['score']
    
    # Threshold check: If similarity is high, use the dataset answer as context
    if score > 0.6:
        retrieved_answer = knowledge_base.iloc[best_hit['corpus_id']]['output']
        
        # Step B: Generation (Use FLAN-T5 to make the answer more conversational)
        prompt = f"Answer this college query based on the info: {user_query}. Info: {retrieved_answer}"
        gen_output = generator(prompt, max_length=100, do_sample=False)
        return gen_output[0]['generated_text']
    
    else:
        return "I'm sorry, I don't have specific information on that. Please contact the admissions office at +91-XXXX-XXXXXX."

# 4. Gradio UI Interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🎓 College Enquiry AI Assistant")
    gr.Markdown("Ask me about admissions, eligibility, documents, or important dates.")
    
    with gr.Row():
        input_text = gr.Textbox(label="Your Question", placeholder="e.g., What is the B.Tech eligibility?")
        
    output_text = gr.Textbox(label="AI Response")
    submit_btn = gr.Button("Ask Assistant")
    
    submit_btn.click(fn=chatbot_response, inputs=input_text, outputs=output_text)

demo.launch(debug=True)
