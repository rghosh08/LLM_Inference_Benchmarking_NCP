# LLM Inference Benchmarking on Nutanix Cloud Platform

## 🤔 What is this?
---
It is a benchmarking study evaluating the inference latency of different models on a given configuration of Nutanix Cloud Platform (NCP). This study covers following models in the HuggingFace repo:

* google/flan-ul2
* cerebras/Cerebras-GPT-13B
* cerebras/Cerebras-GPT-6.7B
* OpenAssistant/oasst-sft-1-pythia-12b
* EleutherAI/pythia-12b
* EleutherAI/gpt-j-6b
* databricks/dolly-v2-12b
* aisquared/dlite-v2-1_5b
* EleutherAI/gpt-j-6b
* mosaicml/mpt-7b
* RedPajama-INCITE-Base-3B-v1
* RedPajama-INCITE-7B-Base
* tiiuae/falcon-7b
* h2oai/h2ogpt-gm-oasst1-en-2048-falcon-7b-v3
* openlm-research/open_llama_7b
* openlm-research/open_llama_13b

## 🚀 Reproducing the Results

You can run the `main.ipy` to recreate the results.

```
  python main.py <hf_model_name> <prompt>
```

## 📚 Read More


* [**HuggingFace**](https://huggingface.co/)
* [**Nutanix Cloud Platform**](https://www.nutanix.com/products)

