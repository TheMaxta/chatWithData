import streamlit as st
import time  # Import time module

chatbot_responses = {
    "How are you?": "I'm doing great, thank you for asking!",
    "What is your name?": "I am a Bot that read the entire Oracle FHIR Documentation text book.",
    "Explain the structure of a Patient resource in FHIR.": """
The Patient resource in FHIR (Fast Healthcare Interoperability Resources) is a JSON object with several properties. Here's a breakdown of the structure:

- "resourceType": This property indicates the type of the resource. In this case, it's "Patient".

- "id": This is the unique identifier assigned to the patient.

- "identifier": This is an array of identifiers used for business purposes. Each identifier object has a "system" property (which is a URI that establishes the system in which the identifier is unique) and a "value" property (which is the unique identifier itself). 

- "name": This is an array of human names for the patient. Each name object can have properties like "family" (for the family or last name) and "given" (for the given or first names).

The Patient resource can also have other properties such as "gender", "birthDate", "address", and so on.  

In addition, the Patient resource can have metadata like "profile" (resource profile declarations) and "securityLabel" (security labels).

When a Patient resource is deleted in FHIR, it's a "logical" delete. The data is not physically removed from the database. Instead, a new version of the resource is created and marked as deleted. This deleted resource no longer appears in search results and attempts to read the resource will fail with an "HTTP 410 Gone" response. However, the original content of the resource is not destroyed and can still be found using FHIR operations like a version-specific read or an instance-history.
"""
    # Add more predefined questions and responses as needed
}
# Function to fetch the bot's response
def get_bot_response(user_input):
    # Return a predetermined response if it exists, else a default response
    return chatbot_responses.get(user_input, "Sorry, I don't have an answer for that. Please ask me another question about FHIR.")

# Initialize session state for storing messages if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I am a Bot that read the entire Oracle FHIR Documentation text book. Please ask me any question about FHIR!"}
    ]

# Display messages
for message in st.session_state.messages:
    if message["role"] == "assistant":
        st.info(message["content"])
    else:
        st.text_area("", value=message["content"], height=50, disabled=True, key=message["content"] + str(st.session_state.messages.index(message)))

# User input
user_input = st.text_input("Your question:", key="user_input")

# Function to handle sending a message
def handle_send():
    if user_input:  # Check if the user has typed anything
        # Append user's question to the conversation
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Simulate bot thinking by waiting for a few seconds
        time.sleep(4)  # Adjust the sleep time as needed

        # Get bot response
        bot_response = get_bot_response(user_input)
        
        # Append bot's response to the conversation
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Clear the input box by resetting its value in the session state
        st.session_state.user_input = ""

# Button to submit the question
if st.button("Send", on_click=handle_send):
    handle_send()
