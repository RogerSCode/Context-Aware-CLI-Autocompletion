from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, LlamaForCausalLM, LlamaTokenizer
import torch
import sys
import os
with open('config.txt', 'r') as f:
    model_name = f.read()

# Load pre-trained model and tokenizer
  



if model_name == "gpt2":
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the autocompletion pipeline
    autocompletion_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        config={"max_new_tokens": 100}  
    )

if model_name == "alpaca":
    #because of its size it should not be downloaded
    base_model = "/path/to/alpaca"
    model = LlamaForCausalLM.from_pretrained(base_model)
    tokenizer = LlamaTokenizer.from_pretrained(base_model)

def list_filenames_as_string(p):
    all_entries = os.listdir(p)
    
    # Filter out directories, keep only files
    filenames = [entry for entry in all_entries if os.path.isfile(entry)]
    
    # Convert the list to a comma-separated string
    filenames_string = ', '.join(filenames)
    
    return filenames_string


input_text = sys.argv[1]


path = sys.argv[2]
files = list_filenames_as_string(path)
premise ="This is a linux terminal."
file_prompt = "There are the following files in the current  directory:" + files 
path_prompt = "Path: " + path
order = "Autocomplete the following linux terminal command and provide no further explanation for the command:"

prompt = premise + file_prompt + path_prompt + order



if model_name == "gpt2":
    completion = autocompletion_pipeline(prompt+input_text, num_return_sequences=1)
    print(completion[0]['generated_text'][len(prompt):])

if model_name == "alpaca":
    input_ids = tokenizer.encode(prompt+input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    prediction = tokenizer.decode(output[0], skip_special_tokens=True)
    print(prediction[len(prompt):])