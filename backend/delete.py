import os
import warnings
import shutil
from get_vector_db import get_vector_db

CHROMA_PATH = os.getenv('CHROMA_PATH', 'chroma')
COLLECTION_NAME = os.getenv('COLLECTION_NAME')
TEXT_EMBEDDING_MODEL = os.getenv('TEXT_EMBEDDING_MODEL')
OLLAMA_HOST = os.getenv('OLLAMA_HOST', 'http://localhost:11434')

# Function to remove the existing database
def delete_persisted_db():
    if "chroma" in os.listdir():
        shutil.rmtree("chroma")
        print(f"Deleted database and its contents.")
    else:
        raise FileNotFoundError("Database not found.")

#def delete_collection(my_collection):
#    db = get_vector_db()
#    count = db.count_collections()
#    if (count != 0)
#        db.delete_collection(name=my_collection)
#        return True
#    return False
    
