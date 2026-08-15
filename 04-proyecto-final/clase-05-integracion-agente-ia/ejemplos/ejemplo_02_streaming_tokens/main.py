"""Generador de Streaming de Tokens."""
def stream_text(txt):
    for word in txt.split(): yield word + ' '
print(list(stream_text('Streaming en tiempo real.')))
