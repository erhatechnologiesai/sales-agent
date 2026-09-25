from fastapi import FastAPI
from app.config import settings
from app.models import ObjectionRequest, ObjectionResponse
from app.services.sales_playbook import resolve_objection

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/handle-objection", response_model=ObjectionResponse)
def handle_objection(req: ObjectionRequest):
    counter, email, next_step = resolve_objection(req.customer_name, req.objection_type, req.customer_statement)
    return ObjectionResponse(
        objection_type=req.objection_type,
        counter_pitch=counter,
        follow_up_email_draft=email,
        proposed_next_step=next_step
    )
