from typing import Dict, List, TypeVar, Generic, Literal, Any, Optional, Union

from pydantic import BaseModel, Field

from .base_types import ReqFetchDataset

T = TypeVar("T")


class ResModel(BaseModel, Generic[T]):
    message: str
    request_id: str
    data: T


class ResLLMFetchDataset(BaseModel):
    """Extract Location Based Information from the Query"""

    query: str = Field(
        default = "",
        description = "Original query passed by the user."
    )
    queryStatus: Literal["Valid", "Invalid"] = Field(
        default="Valid",
        description="Status of the query that depends on approved categories.It must be either 'Valid' or 'Invalid'"
    )
    message: str = Field(
        default = "",
        description = "Response message for the User after processing the query. It helps user to identify issues in the query"
    )
    requestStatus: Literal["Processed", "NotProcessed"] = Field(
        default="NotProcessed",
        description="Set to processed whenever an LLM encounters the query is processed by the LLM"
    )
    fetch_dataset_request: Optional[ReqFetchDataset] = Field(
        default=None,
        description="An object containing detailed request parameters for fetching dataset"
    )
    cost: str = Field(
        default = '',
        description = "The cost value returned by calculate_cost_tool"
    )