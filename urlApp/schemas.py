from pydantic import BaseModel


class PostReqBody(BaseModel):
    url: str
