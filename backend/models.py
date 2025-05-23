from pydantic import BaseModel

class Preferences(BaseModel):
    user_id: str
    job_type: str
    location: str
    is_remote: bool
    is_hybrid: bool
    salary_range: str

