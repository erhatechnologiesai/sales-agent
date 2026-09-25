from pydantic import BaseModel
from typing import List, Optional

class ObjectionRequest(BaseModel):
    customer_name: str
    objection_type: str  # 'pricing', 'security', 'timeline', 'competitor'
    customer_statement: str

class ObjectionResponse(BaseModel):
    objection_type: str
    counter_pitch: str
    follow_up_email_draft: str
    proposed_next_step: str
