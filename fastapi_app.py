from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional
from all_types.myapi_dtypes import ReqLLMFetchDataset, ReqModel
from all_types.response_dtypes import ResModel, ResLLMFetchDataset
from fetch_dataset_llm import process_llm_query
from config_factory import CONF
from backend_common.request_processor import request_handling
app = FastAPI(title="LLM Query API", version="1.0")

@app.post(
    CONF.process_llm_query,
    response_model=ResModel[ResLLMFetchDataset],
)
async def fetch_dataset_ep(req: ReqModel[ReqLLMFetchDataset], request: Request):
    response = await request_handling(
        req.request_body,
        ReqLLMFetchDataset,
        ResModel[ResLLMFetchDataset],
        process_llm_query,
        wrap_output=True,
    )
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
