import requests
import streamlit as st

def get_ollama_response(input_text, endpoint):
    
        # Make the POST request to the specified endpoint
        response = requests.post(
            f"http://localhost:8007/{endpoint}/invoke",
            json={'input': {'topic': input_text}}
        )
        return response.json()["output"]
       

## Streamlit framework setup
st.title('Langchain Demo With LLAMA3.2 API')

# Input fields
input_text1 = st.text_input("Write a poem on")
input_text2 = st.text_input("Start a chat on")

# Display the response for each input
if input_text1:
    st.write(get_ollama_response(input_text1, endpoint="poem"))

if input_text2:
    st.write(get_ollama_response(input_text2, endpoint="chat"))
