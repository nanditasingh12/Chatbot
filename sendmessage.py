from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/sms', methods=['POST'])
def sms_reply():
    """Respond to incoming messages with a simple chatbot."""
    incoming_msg = request.values.get('Body', '').lower()
    response = generate_response(incoming_msg)
    msg = MessagingResponse().message(response)
    return str(msg)

def generate_response(message):
    """Generate a response for the incoming message."""
    # Simple example response based on the received message.
    if 'hello' in message:
        return "Hello, how can I assist you?"
    elif 'help' in message:
        return "Sure, I'm here to help!"
    else:
        return "I'm sorry, I don't understand. Please try again." 
    

if __name__ == '__main__':
    app.run(debug=True) 

