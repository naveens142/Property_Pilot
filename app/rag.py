"""RAG (Retrieval Augmented Generation) for property queries."""

import logging
from qdrant_client import QdrantClient
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from dotenv import load_dotenv

from prompts import PROPERTY_SEARCH_PROMPT, EMPTY_QUESTION_MESSAGE, QUESTION_TOO_LONG_MESSAGE

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize clients
client = QdrantClient(url="http://localhost:6333")
collection_name = "property_docs"
embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_tokens=500)


def ask_question(question: str) -> str:
    """Answer property-related questions using RAG.
    
    Args:
        question: User's property-related question
        
    Returns:
        Response from the LLM
    """
    try:
        # Validate input
        if not question or not question.strip():
            return EMPTY_QUESTION_MESSAGE
        
        if len(question) > 500:
            return QUESTION_TOO_LONG_MESSAGE
        
        # Embed the question
        query_vector = embeddings.embed_query(question)
        
        # Search for relevant documents
        search_results = client.query_points(
            collection_name=collection_name,
            query=query_vector,
            limit=8,
            score_threshold=0.45
        ).points
        
        if not search_results:
            logger.warning(f"No results for query: {question}")
            return "No matching properties found. Try searching by location or property type."
        
        # Build context from search results
        context = "\n\n".join(
            [point.payload['text'] 
             for point in search_results]
        )
        
        # Generate response using LLM
        prompt = PROPERTY_SEARCH_PROMPT.format(context=context, question=question)
        response = llm.invoke(prompt)
        
        logger.info(f"Query: {question} | Results: {len(search_results)}")
        return response.content
        
    except Exception as e:
        logger.error(f"Error processing question '{question}': {str(e)}")
        return "Error processing your query. Please try again."