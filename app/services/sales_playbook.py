PLAYBOOK = {
    "pricing": {
        "counter": "Our multi-agent architectures typically generate 3.8x ROI within the first 90 days by eliminating repetitive manual operations and operational bottlenecks.",
        "next_step": "Offer a 30-day proof-of-concept milestone with guaranteed benchmark targets."
    },
    "security": {
        "counter": "Erha Technologies deploys within your private virtual cloud (VPC) with zero data retention on public LLM provider servers, fully SOC2 and HIPAA compliant.",
        "next_step": "Dispatch security architecture whitepaper and compliance matrix."
    },
    "timeline": {
        "counter": "With our pre-built automation nodes, initial deployment takes under 10 business days without disrupting your live production systems.",
        "next_step": "Provide 2-week implementation sprint timeline."
    }
}

def resolve_objection(name: str, obj_type: str, stmt: str):
    pb = PLAYBOOK.get(obj_type.lower(), PLAYBOOK["pricing"])
    counter = pb["counter"]
    next_step = pb["next_step"]
    
    email = (
        f"Hi {name},\n\n"
        f"Thank you for sharing your thoughts regarding our discussion. In response to your note: '{stmt}', "
        f"{counter}\n\n"
        f"As a next step, I would like to {next_step.lower()}\n\n"
        "Best regards,\nErha AI Sales Solutions"
    )
    return counter, email, next_step
