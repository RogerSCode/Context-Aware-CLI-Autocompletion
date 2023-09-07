from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import itertools
import time
# Load pre-trained model and tokenizer
model_name = "gpt2"  
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Create the autocompletion pipeline
autocompletion_pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=60  
)
prompt ="This is a linux terminal. There are the following files in the current  directory: Path: , Autocomplete the following linux terminal command and provide no further explanation for the command:"
input_list = ["sudo apt","sudo apt up","sudo apt in","ls","py","pyt","pyth","pytho","git","git i","git in","git ini","git co","git comm"]
suggested_completions = []

context = True

files = ["","javasdk.deb","geany.deb","tests.py, data.txt ,webserver.py ","webserver.py,config.txt ",".git, .gitignore, README.md, webserver.py, config.txt, tests.py, data.txt ",]
paths = ["","/home ","/home/user/projekt "]
order = ["Autocomplete the following linux terminal command and provide no further explanation for the command: "]



if context:
    combinations = list(itertools.product(["This is a linux terminal. "],["There are the following files in the current  directory:"],files,paths,order,input_list))



for combination in combinations:
    premise, file_context, files,path, order, input_text = combination

    prompt = premise+file_context+files+path+order+input_text
    print(prompt)
    start_time = time.time()
    completions = autocompletion_pipeline(prompt+input_text, num_return_sequences=1)
    end_time = time.time()
    print("Time: ", end_time-start_time)
    for completion in completions:
        print(completion['generated_text'][len(prompt):])
    suggested_completions.append(completions)
    print("--------------------------------------------------")

