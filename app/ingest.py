from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
import pdfplumber
from dotenv import load_dotenv
import uuid
import os

load_dotenv()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "..", "data", "property_docs.pdf")

# Load PDF
text = ""
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=200
)
chunks = splitter.split_text(text)

# Qdrant client
client = QdrantClient(url="http://localhost:6333")

collection_name = "property_docs"

# Create collection (skip if already exists)
try:
    client.get_collection(collection_name)
    print(f"Collection '{collection_name}' already exists")
except:
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=1536,
            distance=Distance.COSINE
        )
    )
    print(f"Collection '{collection_name}' created")

# Embeddings
embeddings = OpenAIEmbeddings()

# Upsert chunks
points = []
for chunk in chunks:
    vector = embeddings.embed_query(chunk)
    points.append(
        {
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {"text": chunk}
        }
    )

client.upsert(
    collection_name=collection_name,
    points=points
)

print("PDF successfully ingested into Qdrant")
