from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/helloworld')
def get_hello_message():
  return {"message": "Hello World!"}

@app.get('/api/{message}')
def get_any_message(message: str):
  return {"message": message}

class SchemaOfTitanicFeaturesRequest(BaseModel):
  Sex: str
  Pclass: str
  Age: int
  Parch: int
  SibSp: int

@app.post('/api/titanic', response_model=SchemaOfTitanicFeaturesRequest)
def derive_score(request_body: SchemaOfTitanicFeaturesRequest):
  return request_body
