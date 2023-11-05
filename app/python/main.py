from fastapi import FastAPI
from pydantic import BaseModel
from machine_learning.titanic import PredictOnAPI

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

class SchemaOfSurvivalProbabilityResponse(BaseModel):
  survival_probability: float

@app.post('/api/titanic', response_model=SchemaOfTitanicFeaturesRequest)
def derive_score(request_body: SchemaOfTitanicFeaturesRequest):
  # 辞書形式に変更
  features_dict = request_body.__dict__
  # **<辞書オブジェクト>とすることで引数として自動的にバラして与えることが可能
  survival_probability = PredictOnAPI.derive_survival_probability(**features_dict)
  return {'survival_probability': survival_probability}
