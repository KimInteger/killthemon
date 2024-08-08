from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def getHello():
    NAME = "INTEGER"
    print(f"hellow my name is {NAME}")
    
    