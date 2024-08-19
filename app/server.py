from flask import Flask, jsonify, request
from .utils import generate_ticket_response, extract_relevant_response

import json

app = Flask(__name__)


@app.route('/api/crm/tickets/reply/suggestions', methods=['POST'])
def get_ticket_suggestions():
    data = {}
    try:
        data = json.loads(request.data.decode('utf-8'))
        if not data:
            raise ValueError("parameters missing")
    except (json.JSONDecodeError, ValueError) as e:
        return jsonify({'success': False, 'message': f'{str(e)}; help: likely a parameter error'}), 400
    
    try:
        # Fetch ticket details from your CRM database (mocked here)
        ticket_details = {
            "subject": data['subject'],
            "customer_name": data['customer_name'],
            "body": data['body'],
            "agent": data['agent']
        }
    except Exception as e:
        return jsonify({"success": False, "message": f'{str(e)}; help: likely a parameter error'}), 400

    try:
        # Generate AI response using the OpenAIClient
        ai_response = generate_ticket_response(ticket_details)
        extracted_response = extract_relevant_response(ai_response)
        return jsonify({"success": True, **extracted_response})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
