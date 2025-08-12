from db_util import get_db, store_document, get_collection
from util import extract_text_from_pdf
from processing import create_chunk, create_embeddings
import threading 

collection_name = 'documents'


def parse_and_store_pdf(db, pdf_path = "DataScience and AI Resume.pdf"):
    text = extract_text_from_pdf(pdf_path)
    chunks = create_chunk(text, 80, 10)
    
    # Implementing Multi-threading for embedding creation
    for chunk in chunks:
        data = create_embeddings(chunk)
        store_document(db, collection_name, data)
    print(f"Stored Successfully {len(chunks)} chunks in the database.")


def get_similar_document(db, query, top_k=3):
    if len(query.split()) < 200:
        data = create_embeddings(query)
        results = get_collection(db, collection_name, data['embedding'], top_k)
        return results

def main():
    db = get_db()
    query = input("Enter your query: ")
    data = get_similar_document(db, query)
    
    for sent in data:
        print(f"Text:{sent['text']}")
    

    

if __name__ == "__main__":
    main()
