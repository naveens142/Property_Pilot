from qdrant_client import QdrantClient
from pypdf import PdfReader
import os

# Check Qdrant collection
client = QdrantClient(url="http://localhost:6333")

print("=" * 50)
print("QDRANT COLLECTION CONTENTS")
print("=" * 50)

try:
    collection_info = client.get_collection("property_docs")
    print(f"Collection exists with {collection_info.points_count} points")
    print()
    
    # Show first 10 points
    points, _ = client.scroll("property_docs", limit=10)
    print(f"Showing {len(points)} points:\n")
    for i, point in enumerate(points, 1):
        text = point.payload['text'][:150]
        print(f"{i}. {text}...")
        print(f"   Score: {point.score}\n")
except Exception as e:
    print(f"Error: {e}\n")

print("=" * 50)
print("PDF FILE CONTENTS")
print("=" * 50)

# Check PDF content
script_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(script_dir, "data", "property_docs.pdf")

if os.path.exists(pdf_path):
    reader = PdfReader(pdf_path)
    print(f"PDF has {len(reader.pages)} pages\n")
    
    # Show first 500 chars of each page
    for page_num, page in enumerate(reader.pages[:3], 1):
        text = page.extract_text()[:300]
        print(f"Page {page_num}:\n{text}\n---\n")
else:
    print(f"PDF not found at: {pdf_path}")
