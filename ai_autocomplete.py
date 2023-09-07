from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, LlamaForCausalLM, LlamaTokenizer
import torch
import sys



# Load pre-trained model and tokenizer
model_name = "gpt2"  
if model_name == "gpt2":
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the autocompletion pipeline
    autocompletion_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        config={"max_length": 50}  
    )

if model_name == "alpaca":
    base_model = "/path/to/alpaca"
    model = LlamaForCausalLM.from_pretrained(base_model)
    tokenizer = LlamaTokenizer.from_pretrained(base_model)

input_text = sys.argv[1]
files = sys.argv[2]
path = sys.argv[3]
premise ="This is a linux terminal."
file_prompt = "There are the following files in the current  directory:" + files 
path_prompt = "Path: " + path
order = "Autocomplete the following linux terminal command and provide no further explanation for the command:"

prompt = premise + file_prompt + path_prompt + order



 
completion = autocompletion_pipeline(prompt+input_text, num_return_sequences=1)
print(completion['generated_text'][len(prompt):])
