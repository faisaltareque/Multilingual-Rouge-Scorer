from multi_lingual_rouge_score import multi_lingual_rouge
scorer = multi_lingual_rouge.RougeScorer(['rouge1', 'rougeL'], use_stemmer=True)
scores = scorer.score('The quick brown fox jumps over the lazy dog',
                          'The quick brown dog jumps on the log.')

print(scores)