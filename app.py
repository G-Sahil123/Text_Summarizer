# from fastapi import FastAPI
# import uvicorn
# import sys
# import os
# from fastapi.templating import Jinja2Templates
# from starlette.responses import RedirectResponse
# from fastapi.responses import Response
# from TextSummarizer.pipeline.prediction import PredictionPipeline


# text:str = "What is Text Summarization?"

# app = FastAPI()

# @app.get("/", tags=["authentication"])
# async def index():
#     return RedirectResponse(url="/docs")



# @app.get("/train")
# async def training():
#     try:
#         os.system("python main.py")
#         return Response("Training successful !!")

#     except Exception as e:
#         return Response(f"Error Occurred! {e}")
    


# @app.post("/predict")
# async def predict_route(text):
#     try:

#         obj = PredictionPipeline()
#         text = obj.predict(text)
#         return text
#     except Exception as e:
#         raise e
    

# if __name__=="__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8080)

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os
from TextSummarizer.pipeline.prediction import PredictionPipeline


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
import os
from TextSummarizer.pipeline.prediction import PredictionPipeline


# Pydantic model for JSON request
class TextRequest(BaseModel):
    text: str


app = FastAPI()

# Jinja2 template loader
templates = Jinja2Templates(directory="templates")


# Serve UI at root "/"
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Training route
@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return {"message": "Training successful !!"}
    except Exception as e:
        return {"error": str(e)}


# Summarization route
@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(request.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
