import gradio as gr
import requests

API_ENDPOINT = "http://llm-chat:8000/get_input"


def extract_answer(response_text):
    # Tách phần trả lời từ câu trả lời đầy đủ của API
    parts = response_text.split("A: ")
    if len(parts) > 1:
        return parts[-1].strip()
    return response_text


def extract_answer(response_text):
    # Tách phần trả lời từ câu trả lời đầy đủ của API
    parts = response_text.split("A: ")
    if len(parts) > 1:
        return parts[-1].strip()
    return response_text

def chat_with_llm(user_input, chat_history=[]):
    payload = {"input_text": user_input}
    response = requests.post(API_ENDPOINT, json=payload)
    
    if response.status_code == 200:
        llm_response = response.json().get("llama-7b-cpp")
        llm_answer = extract_answer(llm_response)
        chat_history.append(("User", user_input))
        chat_history.append(("LLM", llm_answer))
        return "", chat_history
    else:
        chat_history.append(("Error", "Unable to get a response from the server."))
        return "", chat_history

# Tạo giao diện Gradio với CSS tùy chỉnh
with gr.Blocks(css="""
body {
    background-color: #1e1e1e;
    color: #ffffff;
    font-family: 'Arial', sans-serif;
}

#chatbot {
    height: 500px;
    overflow-y: auto;
    background-color: #2e2e2e;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    color: #ffffff;
}

#user_input {
    border: 1px solid #444;
    border-radius: 15px;
    padding: 10px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
    background-color: #3e3e3e;
    color: #ffffff;
}

#send_button {
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 15px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 10px;
}

#send_button:hover {
    background-color: #45a049;
}
""") as demo:
    gr.Markdown("<h1 style='text-align: center; color: #4CAF50;'>Chat with LLM</h1>")
    
    with gr.Row():
        with gr.Column(scale=4):
            chat_interface = gr.Chatbot(elem_id="chatbot", label="Chat History")
            user_input = gr.Textbox(
                placeholder="Type your message here...",
                lines=1,
                elem_id="user_input"
            )
            send_button = gr.Button("Send", elem_id="send_button")
    
    send_button.click(chat_with_llm, inputs=[user_input, chat_interface], outputs=[user_input, chat_interface])
    user_input.submit(chat_with_llm, inputs=[user_input, chat_interface], outputs=[user_input, chat_interface])

# Khởi chạy ứng dụng Gradio
demo.launch(server_name="0.0.0.0")