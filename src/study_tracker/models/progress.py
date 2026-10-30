from pydantic import BaseModel

class Progress(BaseModel):
    completed_session: int