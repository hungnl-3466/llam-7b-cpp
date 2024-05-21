from llama_cpp import Llama

llm = Llama(
      model_path="app/model/llama-2-7b-chat.Q4_K_M.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)

def llm_process(input_text):
      output = llm(
            "Q: {} A: ".format(input_text), # Prompt
            max_tokens=200, # Generate up to 32 tokens, set to None to generate up to the end of the context window
            stop=["A:", "\n"], # Stop generating just before the model would generate a new question
            echo=True # Echo the prompt back in the output
            ) # Generate a completion, can also call create_completion
      text_output = output["choices"][0]["text"]
      # print(output["choices"][0]["text"])
      return text_output



