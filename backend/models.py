from pydantic import BaseModel
from typing import Optional

class Preferences(BaseModel):
    user_id: str
    job_type: str
    location: str
    is_remote: bool
    is_hybrid: bool
    salary_range: str
    custom_goal: Optional[str] = None  # <-- new optional field
