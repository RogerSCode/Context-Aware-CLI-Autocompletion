import torch
from transformers import  LlamaForCausalLM, LlamaTokenizer
import time


import itertools




# Specify the path to the model directory
model_path = "/gpfs/project/rosel101/"
model_name = "alpaca"
base_model = model_path+model_name
print("model:",model_name)

# check if gpu available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("device:", device)


model = LlamaForCausalLM.from_pretrained(base_model).to(device)
tokenizer = LlamaTokenizer.from_pretrained(base_model)

def print_output(input_text, premises, file_context, files, order, path, autocompleted_text):
    
    print("Input Text:", input_text)
    print("Premise:", premises)
    print("File Context:", file_context)
    print("Files:", files)
    print("Order:", order)
    print("Path:",path)
    print("Autocompleted Text:", autocompleted_text)
    print("--------------------------")

context = True

file_contexts = ["","There are the following files in the current  directory: ", "Files:","These files are in this directory: " ]
files = ["","javasdk.deb","geany.deb","tests.py, data.txt ,webserver.py ","webserver.py,config.txt ",".git, .gitignore, README.md, webserver.py, config.txt, tests.py, data.txt ",]
premises = ["","This is a linux terminal command. ","This is a linux terminal. ","You are an autocomplete function. ","This is an autocomplete function. "]
paths = ["","/home ","/home/user/projekt "]
order = ["Autocomplete the following linux terminal command and provide no further explanation for the command: "]
input_texts =["sudo apt","sudo apt up","sudo apt in","ls","py","pyt","pyth","pytho","git","git i","git in","git ini","git co","git comm"]

combinations = list(itertools.product(premises, file_contexts, files, paths, order, input_texts))
final_prompt = "This is a linux terminal. There are the following files in the current  directory:,Path:, Autocomplete the following linux terminal command and provide no further explanation for the command:"





if context:
    combinations = list(itertools.product(["This is a linux terminal. "],["There are the following files in the current  directory:"],files,paths,order,input_texts))



for combination in combinations:
    premise, file_context, files,path, order, input_text = combination
    prompt = premise+file_context+files+path+order+input_text
    input_ids = tokenizer.encode(prompt, return_tensors="pt").to(device)
    start_time = time.time()
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, do_sample=True)
    end_time = time.time()
    print("Time: ", end_time-start_time)
    prediction = tokenizer.decode(output[0], skip_special_tokens=True)
    autocompleted_text=prediction[len(prompt)-len(input_text):]
    print_output(input_text, premise, file_context, files, order, path, autocompleted_text,)
 