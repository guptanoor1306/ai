import streamlit as st
import requests

# Set your OpenAI API key
api_key = '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'

def main():
    st.title("AI Number Adder with GPT")

    # Create input boxes for numbers
    num1 = st.number_input("Enter the first number:", key="num1")
    num2 = st.number_input("Enter the second number:", key="num2")

    # Button to trigger the addition
    if st.button("Add Numbers"):
        # Constructing the prompt to send to GPT
        prompt = f"What is the sum of {num1} and {num2}?"
        # Calling GPT to process the prompt
        response = get_response(prompt)
        # Display the result or error
        if 'choices' in response and len(response['choices']) > 0 and 'text' in response['choices'][0]:
            st.write("AI: ", response['choices'][0]['text'].strip())
        else:
            st.write("AI: An error occurred. Please try again.")

def get_response(prompt):
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
        return response.json()
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return {}

if __name__ == "__main__":
    main()
