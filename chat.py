import os
import openai
import streamlit as st

# Set the OpenAI API key and the GPT-3.5-Turbo model engine
openai.api_key = st.secrets["OPENAI_API_KEY"]
model_engine = "gpt-3.5-turbo"

# Define a function to generate responses using GPT-3.5-Turbo
def generate_response(prompt, temperature=0.5):
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system", "content": "I am a Japanese Teacher."},
                  {'role': 'user', 'content': prompt}],
        max_tokens=1024,
        temperature=temperature
    )
    return response.choices[0].message.content

# Define the main function to handle the user input and generate responses
def main():
    # Set the page title
    st.title("日语聊天工具")

    # Get user input
    user_input = st.text_input("请输入您的消息", "")

    # Generate response
    if user_input:
        response = generate_response("用户: " + user_input + "\nAI: ")
        st.text_area("AI回复", value=response, height=200, max_chars=None)

# Run the app
if __name__ == "__main__":
    main()
