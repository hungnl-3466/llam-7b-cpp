from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys
from pydantic import BaseModel

sys.path.insert(0, 'app')
from infrastructure.llama_cpp_infer import llm_process

app  = FastAPI()    

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class InputData(BaseModel):
    input_text: str
    
@app.post("/get_input")
async def get_input(data: InputData):   
    input_text = data.input_text
    print(input_text)
    output = llm_process(input_text)
    return JSONResponse(status_code=200, content={"llama-7b-cpp": output})

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)