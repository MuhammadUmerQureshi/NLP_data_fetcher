from typing import Dict, List, TypeVar, Generic, Optional, Literal

from pydantic import BaseModel, Field

U = TypeVar("U")

class Coordinate(BaseModel):
    lat: Optional[float] = None
    lng: Optional[float] = None


class ReqUserId(BaseModel):
    user_id: str


class ReqModel(BaseModel, Generic[U]):
    message: str
    request_info: Dict
    request_body: U


class ReqCityCountry(BaseModel):
    city_name: str
    country_name: str

class ReqPrdcerLyrMapData(ReqUserId):
    prdcer_lyr_id: Optional[str] = ""


class ReqFetchDataset(ReqCityCountry, ReqPrdcerLyrMapData, Coordinate):
    boolean_query: Optional[str] = ""
    action: Optional[str] = ""
    page_token: Optional[str] = ""
    search_type: Optional[str] = "default"
    text_search: Optional[str] = ""
    zoom_level: Optional[int] = 0
    radius: Optional[float] = 30000.0
    _bounding_box: Optional[list[float]] = []
    _included_types: Optional[list[str]] = []
    _excluded_types: Optional[list[str]] = []


class ReqLLMFetchDataset(BaseModel):
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