from .ai_clients import *

def get_ai_client(client_type="groq"):
    if client_type == "groq":
        return GroqClient()
    elif client_type == "openai":
        return OpenAIClient()
    else:
        raise ValueError("Unsupported client type")
    
def generate_ticket_response(ticket_details):
    # Construct the prompt
    ai_client = get_ai_client(client_type="groq")

    prompt = f"""
    You are a helpful support agent. Here's a ticket:
    Subject: {ticket_details['subject']}
    Created at: {ticket_details['created_at']}
    Customer: {ticket_details['customer_name']}
    Issue: {ticket_details['issue']}
    
    Suggest a helpful response.
    """

    # Use OpenAIClient to generate the response
    ai_response = ai_client.generate_response(prompt)
    return ai_response
