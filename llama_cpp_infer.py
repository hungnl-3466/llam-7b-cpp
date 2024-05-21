from llama_cpp import Llama

llm = Llama(
      model_path="llama-2-7b-chat.Q4_K_M.gguf",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      # seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
      "Q: What is the name of the biggest company in the worlds? A: ", # Prompt
      max_tokens=100, # Generate up to 32 tokens, set to None to generate up to the end of the context window
      stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
      echo=True # Echo the prompt back in the output
) # Generate a completion, can also call create_completion
print(output["choices"][0]["text"])