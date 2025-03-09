from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "診察管理APIが動いています"}

@app.get("/next_patient/")
def next_patient():
    return {"診察する患者": "現在の患者を表示する処理（後で追加）"}
