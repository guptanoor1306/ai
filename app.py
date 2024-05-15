import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

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
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  # Update this with the model you have access to
            prompt=prompt,
            max_tokens=50
        )
        return response
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

if __name__ == "__main__":
    main()
