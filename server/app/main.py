from fastapi import FastAPI
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

app = FastAPI()

PORT = int(os.getenv("CLI_PORT"))

@app.get("/")
def hello() :
    print("hellow wolrd")


if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True )
