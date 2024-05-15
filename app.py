import streamlit as st
import openai

# Initialize session state to store conversation
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

# Set your OpenAI API key
openai.api_key = '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'

def main():
    st.title("Interactive AI Chat")

    # Text-to-speech script
    st.markdown("""
        <script src="https://code.responsivevoice.org/responsivevoice.js?key=yourKey"></script>
        """, unsafe_allow_html=True)

    # Display the conversation history
    for idx, part in enumerate(st.session_state['conversation']):
        speaker, text = part
        st.text_area(f"{speaker} says:", value=text, height=100, key=str(idx), disabled=True)
    
    # User input
    user_input = st.text_input("Your message:", key="user_input")

    # Send button
    if st.button("Send"):
        if user_input:
            # Update conversation history
            update_conversation("You", user_input)

            # Get response from OpenAI GPT
            response = get_response(user_input)
            update_conversation("AI", response)

            # Speak the response
            speak(response)

            # Clear input
            st.session_state['user_input'] = ""

def update_conversation(speaker, message):
    st.session_state['conversation'].append((speaker, message))

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Adjust according to your API plan
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

def speak(text):
    st.markdown(
        f"""
        <script>
        responsiveVoice.speak("{text}", "US English Female");
        </script>
        """, unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
