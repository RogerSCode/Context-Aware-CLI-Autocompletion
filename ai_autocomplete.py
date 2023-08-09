from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Load pre-trained model and tokenizer
model_name = "gpt2"  
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the autocompletion pipeline
autocompletion_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    config={"max_length": 50}  
)
prompt ="This is a linux terminal. There are the following files in the current  directory: Path: , Autocomplete the following linux terminal command and provide no further explanation for the command:"
#input_list = ["sudo apt", "Autocomplete: sudo apt ", "sudo apt ins","git i","git ini","Autocomplete the following terminal command: git c","git comm"]
input_list = ["sudo apt","sudo apt up","sudo apt in","ls","py","pyt","pyth","pytho","git","git i","git in","git ini","git co","git comm"]
suggested_completions = []

# Generate completions for each input item
for input_text in input_list:
    completions = autocompletion_pipeline(prompt+input_text, num_return_sequences=3)
    suggested_completions.append(completions)

# Print the suggested completions
for i, completions in enumerate(suggested_completions):
    print(f"Completions for input {i+1}:")
    for j, completion in enumerate(completions):
        print(f"Suggested completion {j+1}: {completion['generated_text'][len(prompt):]}")
