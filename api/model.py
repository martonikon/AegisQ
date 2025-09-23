from pydantic import BaseModel

class JobPayload(BaseModel):
    task_type: str
    payload: dict