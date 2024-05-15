import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = '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'

def main():
    st.title("Interactive AI Chat with GPT-3.5 Turbo")

    # Load text-to-speech JavaScript
    st.markdown("""
        <script src="https://code.responsivevoice.org/responsivevoice.js?key=yourKey"></script>
        """, unsafe_allow_html=True)

    # Initialize session state to store conversation history
    if 'conversation' not in st.session_state:
        st.session_state['conversation'] = []

    # Display the conversation history
    for idx, part in enumerate(st.session_state['conversation']):
        speaker, text = part
        st.text_area(f"{speaker} says:", value=text, height=100, key=str(idx), disabled=True)
    
    # User input
    user_input = st.text_input("Your message:", key="user_input")

    # Send button
    if st.button("Send") and user_input:
        # Update conversation history
        update_conversation("You", user_input)

        # Get response from OpenAI GPT
        response = get_response(user_input)
        update_conversation("AI", response)

        # Speak the response
        speak(response)

        # Clear input
        st.session_state.user_input = ""

def update_conversation(speaker, message):
    """Updates the conversation history in the session state."""
    st.session_state['conversation'].append((speaker, message))

def get_response(prompt):
    """Gets a response from the GPT-3.5 Turbo model."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify the model
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()

def speak(text):
    """Uses ResponsiveVoice to convert text to speech."""
    st.markdown(
        f"""
        <script>
        responsiveVoice.speak("{text}", "US English Female");
        </script>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
