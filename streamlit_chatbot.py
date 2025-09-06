import streamlit as st
openai_api_key = st.secrets("OPENAI_API_KEY")
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS

# Load the QLoRA model (or any fine-tuned language model)
llm = ChatOpenAI(model_name="gpt-3.5-turbo")

# Load FAISS vector store
vectorstore = FAISS.load_local("vectorstore.db")
retriever = vectorstore.as_retriever()

def get_qlora_response(prompt: str) -> str:
    """
    Generate a response using QLoRA-based model and return the response.

    Parameters:
    prompt (str): The user's input/question for the model.

    Returns:
    str: The model's response, possibly split if too long.
    """
    # Retrieve the relevant documents based on the input prompt
    retrieved_docs = retriever.get_relevant_documents(prompt)

    # Combine the retrieved documents with the prompt (context)
    context = "\n".join([doc.page_content for doc in retrieved_docs])  # Access the text content
    full_prompt = f"{context}\n\n{prompt}"

    # Generate the response using QLoRA and the combined prompt
    response = llm.predict(text=full_prompt)

    # Check if the response length exceeds a certain limit, and split it
    max_length = 500  # Maximum length before splitting
    if len(response) > max_length:
        mid_point = len(response) // 2
        response_part1 = response[:mid_point]
        response_part2 = response[mid_point:]

        return f"Chatbot (Part 1): {response_part1}\n\nChatbot (Part 2): {response_part2}"
    else:
        return f"Chatbot: {response}"
		

# Streamlit app UI
st.title("QLoRA Chatbot")
st.write("Ask anything about QLoRA or any other topic you're curious about!")

# Text input from the user
user_input = st.text_input("You:", "")

if user_input:
    # Get response from QLoRA model
    answer = get_qlora_response(user_input)
    st.write(answer)