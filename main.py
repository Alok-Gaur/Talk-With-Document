from tools import parse_and_store_pdf, get_similar_document
from smolagents import LiteLLMModel, ToolCallingAgent


def main():
    model = LiteLLMModel(
        model_id = "ollama/qwen3:0.6b",
        api_base= "http://127.0.0.1:11434",
        num_ctx = 3192,
    )
    
    initial_prompt = """
    You are a helpful and intelligent QnA assistant. Your job is to answer user questions based strictly on the suggestions (knowledge snippets) provided to you. 
    You must not use any external knowledge or make assumptions beyond the given suggestions.

     Instructions:
        1. Use Only Provided Suggestions:
            Do not invent or infer information. If the answer is not found in the suggestions, respond accordingly.
        2. Be Clear and Concise:
            Use simple, direct language. Avoid jargon unless it's explained.
        3. Respect the Format:
            Always follow the response format below.
        4. Tone:
            Friendly, professional, and informative.

    Input format:
        {
            "question": "User's question here",
            "suggestions": [
                "Relevant suggestion 1",
                "Relevant suggestion 2",
                "Relevant suggestion 3"
            ]
            }

    """

    agent = ToolCallingAgent(tools=[], model=model, instructions=initial_prompt)
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break

        suggestions = get_similar_document(user_input)

        user_prompt = f"""
        "question": {user_input},
        "suggestions":{suggestions}
        """

        
        response = agent.run(user_prompt)
        
        if response:
            print(f"Assistant: {response}")
        else:
            print("Assistant: No response generated.")
    
    
    
    

if __name__ == "__main__":
    upload_pdf = input("Upload Pdf? Enter [y] Yes or [n] No: ").lower()

    if upload_pdf in  ('y', 'yes'):
        path =  input("Enter PDF path: ")
        if path:
            print(parse_and_store_pdf(path))
            main()
        else:
            print("No path provided. Try again!")
    else:
        main()




##This is initial codes for testing and implementing
# collection_name = 'documents'


# def parse_and_store_pdf(db, pdf_path = "DataScience and AI Resume.pdf"):
#     text = extract_text_from_pdf(pdf_path)
#     chunks = create_chunk(text, 60, 10)
    
#     for chunk in chunks:
#         data = create_embeddings(chunk)
#         print("embedding created!")
#         store_document(db, collection_name, data)
    
#     print(f"Stored Successfully {len(chunks)} chunks in the database.")


# def get_similar_document(db, query, top_k=3):
#     if len(query.split()) < 200:
#         data = create_embeddings(query)
#         results = get_collection(db, collection_name, data['embedding'], top_k)
#         return results

# def main():
#     db = get_db()
#     print('parsing and storing pdf...')
#     parse_and_store_pdf(db, "47303.pdf")
#     query = input("Enter your query: ")
#     response = get_similar_document(db, query)
    
#     content = []
#     for sentence in response:
#         content.append(sentence['text'])
    
#     print(content)
#     # Demo change

    