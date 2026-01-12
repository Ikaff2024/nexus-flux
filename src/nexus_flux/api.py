from fastapi import FastAPI
from .engine import Engine
app=FastAPI()
@app.post('/solve')
def solve(): return {'result': Engine().run()}
