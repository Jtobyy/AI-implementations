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
    Customer: {ticket_details['customer_name']}
    Body: {ticket_details['body']}
    Agent Name: {ticket_details['agent']}
    
    Suggest a helpful response.
    """

    # Use OpenAIClient to generate the response
    ai_response = ai_client.generate_response(prompt)
    return ai_response

def extract_relevant_response(ai_response):
    # Find the position of the "Re" part (or any specific part you want)
    start_index = ai_response.find("Re")
    
    # If found, extract the relevant portion; otherwise, return the full response
    if start_index != -1:
        relevant_response = ai_response[start_index:]
    else:
        relevant_response = ai_response  # Or handle it differently based on your needs
    
    # Construct the dictionary with the relevant part
    response_dict = {"suggested_response": relevant_response}
    
    return response_dict