from smolagents import tool
from db_util import store_document, get_collection, get_db
from util import extract_text_from_pdf
from processing import *

db = get_db()
collection_name = 'documents'


@tool
def parse_and_store_pdf(pdf_path:str = "DataScience and AI Resume.pdf") ->str:
    """Parse the PDF file and store its content in the database.

    Args:
        pdf_path (str, optional): Path to local storage. Defaults to "DataScience and AI Resume.pdf".

    Returns:
        str: Status message indicating success or failure.
    """
    try:
        text = extract_text_from_pdf(pdf_path)
        chunks = create_chunk(text, 80, 10)
        
        # Implementing Multi-threading for embedding creation
        for chunk in chunks:
            data = create_embeddings(chunk)
            store_document(db, collection_name, data)
        return f"Stored Successfully {len(chunks)} chunks in the database."
    except Exception as e:
        return f"Error occured: {str(e)}"

@tool
def get_similar_document(query:str, top_k:int=3)-> List[str]:
    """Query the similar topics from the database based on the user query.

    Args:
        query (str): User query to find similar content on document
        top_k (int, optional): Top k relevent chunks available in the database. Defaults to 3.

    Returns:
        List[str]: Top k similar content from the document.
        If no similar content found, returns a message indicating that.
    """
    try:
        if len(query.split()) < 200:
            data = create_embeddings(query)
            results = get_collection(db, collection_name, data['embedding'], top_k)
            if results:
                return [sentences['text'] for sentences in results]
            return "No similar content found in document."
        else:
            return "Query is too long, please provide a shorter query."
    except Exception as e:
        return f"Error occurred: {str(e)}"    
