# Multilingual ROUGE([Rouge_score](https://github.com/google-research/google-research/tree/master/rouge)) Scoring Using BPE Tokenizer 

This repo extended from [
multilingual-rouge](https://github.com/KaiQiangSong/multilingual-rouge).
  


## Setup from Clone
```bash
python setup.py bdist_wheel
pip install -e .
```

## Setup from Git
```bash
pip install https://github.com/faisaltareque/multi_lingual_rouge_BPE_tokenizer
```


* **Default usage**


```python
from multi_lingual_rouge_score import multi_lingual_rouge
scorer = multi_lingual_rouge.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog',
                          'The quick brown dog jumps on the log.')
```
