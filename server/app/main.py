from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse, PlainTextResponse
from dotenv import load_dotenv
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

index_html_path = Path(__file__).resolve().parent.parent.parent / 'index.html'
bundle_js_path = Path(__file__).resolve().parent.parent.parent / 'dist/index.bundle.js'

app = FastAPI()

PORT = int(os.getenv("CLI_PORT"))

@app.get("/")
async def hello() :
    try : 
        logger.info("serving index.html")
        with open(index_html_path, 'r') as file :
            return HTMLResponse(content=file.read(), status_code=200)
    except Exception as e:
        logger.error(f"Error serving index.html : {str(e)}")
        return HTMLResponse(content=f"Error: {str(e)}", status_code=500)

@app.get("/dist/index.bundle.js")
async def getdist() :
    try : 
        logger.info("serving bundle.js")
        return FileResponse(path=bundle_js_path, media_type="application/javascript")
    except Exception as e:
        logger.error(f"Error serving index.html : {str(e)}")
        return PlainTextResponse(content=f"Error: {str(e)}", status_code=500)
    


if __name__ == '__main__' :
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True )
