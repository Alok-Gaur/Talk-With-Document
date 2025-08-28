from db_util import get_db, store_document, get_collection
from util import extract_text_from_pdf
from processing import create_chunk, create_embeddings
from tools import parse_and_store_pdf, get_similar_document
from smolagents import LiteLLMModel, ToolCallingAgent, ChatMessage


def main():
    model = LiteLLMModel(
        model_id = "ollama/qwen3:0.6b",
        api_base= "http://127.0.0.1:11434",
        num_ctx = 3192,
    )
    
    agent = ToolCallingAgent(tools=[get_similar_document], model=model, instructions="You must always call the `get_similar_document` tool to retrieve relevant document context before answering and give anwer to the user query based on the retrieved context. If no relevant context is found, respond with 'No relevant documents found.'")
    
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chat.")
            break
        
        response = agent.run(user_input)
        
        if response:
            print(f"Assistant: {response}")
        else:
            print("Assistant: No response generated.")
    
    
    
    
    
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
    
    # content = []
    # for sentence in response:
    #     content.append(sentence['text'])
    
    # Demo change

    

    

if __name__ == "__main__":
    main()
