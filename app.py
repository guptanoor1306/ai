import streamlit as st
import requests

def get_response(prompt, api_key):
    try:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "max_tokens": 50
        }
        response = requests.post("https://api.openai.com/v1/completions", json=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}: {response.text}"}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def main():
    st.title("AI Number Adder with GPT")

    # Set your OpenAI API key
    api_key = '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'

    # Create input boxes for numbers
    num1 = st.number_input("Enter the first number:", key="num1")
    num2 = st.number_input("Enter the second number:", key="num2")

    # Button to trigger the addition
    if st.button("Add Numbers"):
        # Constructing the prompt to send to GPT
        prompt = f"Calculate the sum of {num1} and {num2}."
        # Calling GPT to process the prompt
        response = get_response(prompt, api_key)
        # Display the result or error
        if 'choices' in response and len(response['choices']) > 0 and 'text' in response['choices'][0]:
            st.write("AI: ", response['choices'][0]['text'].strip())
        elif 'error' in response:
            st.write("AI: An error occurred:", response['error'])
        else:
            st.write("AI: Unable to retrieve a response from the API.")

if __name__ == "__main__":
    main()
