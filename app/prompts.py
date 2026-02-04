"""Prompt templates for the property chatbot."""

PROPERTY_SEARCH_PROMPT = """You are a property consultant. Show ONLY the most relevant properties matching the query.

Available Properties:
{context}

Client Question: {question}

INSTRUCTIONS:
1. Show ONLY properties that match the user's query
2. For each matching property, display in this EXACT format with line breaks:

Property Name:
Location:
Description:
Area:
Budget/Price:
Features/Suitability:

3. NEVER show properties that don't match the search criteria
4. Use clear line breaks between each property
5. Do NOT write in paragraph format - use the structured format above
6. Include ALL fields for each property

Response:"""

NO_RESULTS_MESSAGE = """No matching properties found for your search. 

Try searching with:
- Specific locations (e.g., "Bangalore", "Mumbai", "Chennai")
- Property types (e.g., "apartment", "villa", "commercial office")
- Price ranges (e.g., "under 50 lakhs", "above 1 crore")
- Features (e.g., "swimming pool", "garden", "parking")

Example searches: "2BHK flats in Bangalore" or "Commercial space in Hyderabad"""

EMPTY_QUESTION_MESSAGE = "Please ask a property-related question. For example: 'Show me 2BHK apartments in Bangalore under 50 lakhs'"

QUESTION_TOO_LONG_MESSAGE = "Your question is too long. Please keep it under 500 characters."

SYSTEM_ERROR_MESSAGE = "Error processing your query. Please try again or contact support."
