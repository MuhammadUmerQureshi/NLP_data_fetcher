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
