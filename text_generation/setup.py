import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration,Adafactor, T5Model

tokenizer = T5Tokenizer.from_pretrained('t5-small', cache_dir="/tmp/")
model = T5ForConditionalGeneration.from_pretrained('t5-small',
                                             return_dict=True,
                                             cache_dir="/tmp/")
