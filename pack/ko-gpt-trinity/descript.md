The tokenizer class you load from this checkpoint is not the same type as the class this function is called from. It may result in unexpected tokenization. 
The tokenizer class you load from this checkpoint is 'GPT2Tokenizer'. 
The class this function is called from is 'PreTrainedTokenizerFast'.


# PreTrainedTokenizerFast 를 쓰자 아래와 같은 경고 메시지를 받았다.
Hugging Face의 transformers 라이브러리에서 AutoTokenizer를 사용하면 
모델에 적합한 토크나이저를 자동으로 로드할 수 있다고 한다.
AutoTokenizer 를 사용하고, 모델에 적합한 토크나이저를 확인하자.
print(f"Loaded tokenizer class: {tokenizer.__class__.__name__}")
>> 결과: GPT2TokenizerFast

GPT2Tokenizer 가 아닌 GPT2TokenizerFast 를 사용하자,
GPT2Tokenizer 이용시에는 보이지 않았던, merges.txt, vocab.json 도 나왔다.

참고로, 사용 중인 모델은
config.json 에서 확인하였다.
"architectures": [
    "GPT2LMHeadModel"
],

# model의 config.json 에서 eos 토큰과 pad 토큰이 같게 설정 되어있는 문제.
혹시 몰라서 AutoModel 을 사용해 모델을 다운받았지만 (GPT2LMHeadModel 이 아닌 GPT2Model 이 로드됨)
config.json 의 설정은 같았다. 
어떤 클래스를 이용해서 다운 받는 지는 학습된 모델의 설정에 영향을 미치지 않는 것 같다..

아래와 같이 생성되어, unk 토큰 (5) 을 eos_token 으로 generate 시에 넣어도 멈추지 않았다.
>> 생성된 문장:
>  개발곰은 귀엽다. 왜냐하면, 이 곰을 보고 있노라면 나도 모르게 웃음이 나기 때문이다. 귀여운 외모와 달리 털이 복실복실한 것이 귀여워 보이기까지 한다. 
 <unk>
> 
> 모델의 eos 토큰이 맞지 않아서 일까..?