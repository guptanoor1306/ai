import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

def main():
    st.title("OpenAI GPT-4o Chat")

    # Initial message from AI
    st.write("AI: Hi there! What do you want to do?")
    user_input = st.text_input("You: ")

    if user_input.lower() == "i want to add 2 numbers":
        st.write("AI: Sure, tell me the first number:")
        num1 = st.number_input("You: ")
        st.write("AI: Okay, second number:")
        num2 = st.number_input("You: ")

        # Calculate sum
        total = num1 + num2
        st.write(f"AI: The total is {total}")

if __name__ == "__main__":
    main()

