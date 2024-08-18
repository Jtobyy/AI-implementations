from flask import Flask, jsonify
from .utils import generate_ticket_response

app = Flask(__name__)


@app.route('/api/crm/tickets/reply/suggestions', methods=['GET'])
def get_ticket_suggestions():
    # Fetch ticket details from your CRM database (mocked here)
    ticket_details = {
        "subject": "Unable to login to account",
        "created_at": "2024-08-15T10:00:00Z",
        "customer_name": "John Doe",
        "issue": "The user reports being unable to log in with their credentials."
    }

    try:
        # Generate AI response using the OpenAIClient
        ai_response = generate_ticket_response(ticket_details)
        return jsonify({"suggested_response": ai_response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
