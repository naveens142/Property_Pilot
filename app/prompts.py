"""Prompt templates for the property chatbot."""

PROPERTY_SEARCH_PROMPT = """You are a friendly property consultant helping clients find their ideal property.

Available Properties:
{context}

Client Question: {question}

Provide a helpful, conversational response that:
- Directly answers their question with specific property details
- Highlights key information (price, location, size, features, amenities)
- Explains why the property matches their needs
- Uses a warm, professional tone
- Suggest next steps (viewing, payment plans, etc.)
- If no match, suggest alternative searches they could try

Keep response concise, friendly, and client-focused. Avoid technical jargon."""

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
