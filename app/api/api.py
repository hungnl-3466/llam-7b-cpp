from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app  = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/get_input")
async def get_input(input_text: str= Form()):
    return JSONResponse(status_code=200, content={"input": input_text})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)