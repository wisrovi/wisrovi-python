"""Ranking de Relevancia Semántica."""
docs = [{'txt':'Python code', 'score': 0.95}, {'txt':'Pizza recipe', 'score': 0.10}]
print('Top 1:', sorted(docs, key=lambda x: x['score'], reverse=True)[0])
