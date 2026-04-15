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

pipeline = None

@app.on_event("startup")
async def load_model():
    global pipeline
    pipeline = PredictionPipeline()

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
        summary = pipeline.predict(request.text)
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
