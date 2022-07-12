from selectors import BaseSelector


from pydantic import BaseModel, Field


class PostReqBody(BaseModel):
    url: str


