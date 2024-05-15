import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

def main():
    st.title("OpenAI GPT Chat")

    conversation = st.session_state.get('conversation', [])
    
    # Display previous parts of the conversation
    for part in conversation:
        st.text_area("", value=part, height=80, disabled=True)
    
    user_input = st.text_input("Ask me anything!", key="input", on_change=clear_input_box)

    if st.button("Send") or user_input:
        if user_input:
            conversation.append("You: " + user_input)
            st.session_state.conversation = conversation
            response = openai.Completion.create(
                engine="davinci", 
                prompt=user_input,
                max_tokens=150
            )
            answer = response.choices[0].text.strip()
            conversation.append("AI: " + answer)
            st.session_state.conversation = conversation
            st.session_state.input = ""

def clear_input_box():
    st.session_state.input = ""

if __name__ == "__main__":
    main()
