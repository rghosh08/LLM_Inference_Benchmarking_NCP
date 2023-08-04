from transformers import pipeline
import sys
import time
from transformers import AutoTokenizer, AutoModelForCausalLM

def model_perf():
    start = time.time()
    tokenizer = AutoTokenizer.from_pretrained(sys.argv[1])
    model = AutoModelForCausalLM.from_pretrained(sys.argv[1])
    
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    generated_text = pipe(sys.argv[2], max_length=50, do_sample=False, no_repeat_ngram_size=2)[0]
    print(time.time()-start)
    return generated_text

if __name__=="__main__":
    print(model_perf())
