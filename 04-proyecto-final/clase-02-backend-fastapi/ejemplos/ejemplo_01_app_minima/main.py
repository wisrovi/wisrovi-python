"""API Mínima con FastAPI."""
from fastapi import FastAPI
app = FastAPI()
@app.get('/ping')
def ping(): return {'status': 'ok'}
print('FastAPI app configurada.')
