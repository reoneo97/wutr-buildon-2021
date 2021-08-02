import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration,Adafactor, T5Model

tokenizer = T5Tokenizer.from_pretrained('t5-small',cache_dir="/tmp/")
model = T5ForConditionalGeneration.from_pretrained('t5-small',
                                             return_dict=True,
                                             cache_dir="/tmp/")



path = 'stronks_tg.pt'
model.load_state_dict(torch.load(path,map_location=torch.device('cpu')))

def generate(text):
  model.eval()
  input_ids = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length',max_length=10).input_ids  # Batch size 1
  outputs = model.generate(input_ids,max_length = 30,do_sample=True,top_k=530,top_p=0.95,num_return_sequences=1)
  gen_text=tokenizer.decode(outputs[0],skip_special_tokens=True)  
  return gen_text

def lambda_handler(event, context):
    input_text = event["text"]
    try: 
        output_desc = generate(input_text)
        response = {
            "statusCode": 200,
            "body": output_desc
        }
    except:
        response = {
            "statusCode": 404,
            "body": f"{input_text*3}"
        }

    return response
