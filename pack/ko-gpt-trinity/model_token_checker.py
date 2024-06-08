from transformers import GPT2LMHeadModel, GPT2TokenizerFast
import os
import torch

model_dir = "../../model/pretrained/skt/ko-gpt-trinity-1.2B-v0.5"

# Fx 3. local 의 model 과 tokenizer load 하여 토큰 설정 확인
model = GPT2LMHeadModel.from_pretrained(model_dir)
tokenizer = GPT2TokenizerFast.from_pretrained(model_dir)
# 모델의 전체 구성 출력
model_config = model.config
print(model_config)
# Step 1. 모델 구성과 토크나이저 설정 확인
model_config = model.config
print(f"Model BOS Token ID: {model_config.bos_token_id}, token name: {tokenizer.decode(model_config.bos_token_id)}")
print(f"Model EOS Token ID: {model_config.eos_token_id}, token name: {tokenizer.decode(model_config.eos_token_id)}")
print(f"Model PAD Token ID: {model_config.pad_token_id}, token name: {tokenizer.decode(model_config.pad_token_id)}")

print(f"Tokenizer BOS Token ID: {tokenizer.bos_token_id}, token name: {tokenizer.decode(tokenizer.bos_token_id)}")
print(f"Tokenizer EOS Token ID: {tokenizer.eos_token_id}, token name: {tokenizer.decode(tokenizer.eos_token_id)}")
print(f"Tokenizer PAD Token ID: {tokenizer.pad_token_id}, token name: {tokenizer.decode(tokenizer.pad_token_id)}")
