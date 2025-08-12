from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from typing import List, Dict

def create_chunk(text, chunk_size=200, overlap=30) -> List[str]:
    """    Splits the input text into chunks of specified size and overlap.

    Args:
        text (str): Original text to be split into chunks.
        chunk_size (int, optional): Size of each chunk. Defaults to 200.
        overlap (int, optional): Tokens that are shared between consecutive chunks. Defaults to 30.
    """
    tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
    token = tokenizer.encode(text, add_special_tokens=False)
    
    chunks = []
    for i in range(0, len(token), chunk_size - overlap):
        chunk = token[i:i + chunk_size]
        if len(chunk) < chunk_size:
            break
        chunks.append(tokenizer.decode(chunk, skip_special_tokens=True))
    return chunks

def create_embeddings(text) -> Dict[str, List[float]]:
    """Creates embeddings for a list of texts using a pre-trained model.

    Args:
        texts (List(str)): List of texts to create embeddings for.
    
    Returns:
        text: Text for which embedding created.
        embedding: Embedding vector for the text.
        
    """
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(text, show_preprocessing=True, convert_to_tensor=False, normalize_embeddings=True).tolist()
    return {
        "text": text,
        "embedding": embeddings
    }
    