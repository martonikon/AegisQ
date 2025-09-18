import json
from uuid import uuid4

from fastapi import APIRouter

from api.redis_setup import redis_plug as r
from api.model import JobPayload

router = APIRouter()

@router.post('/submit_job')
def submit_job(job: JobPayload):
    job_id = str(uuid4())
    
    job_stats = {
        'id': job_id,
        'type': job.task_type,
        'payload': job.payload
    }

    r.lpush("job_queue", json.dumps(job_stats))
    
    r.set(f'status:{job_id}', 'queued')
    
    return {'job_id': job_id, 'status': 'queued'}

@router.get('/status/{job_id}')
def get_status(job_id: str):
    status = r.get(f'status:{job_id}')
    if status:
        return {'job_id': job_id, 'status': status}
    
    return {'error': 'Job not found'}

@router.get("/result/{job_id}")
def get_result(job_id: str):
    raw_result = r.get(f"result:{job_id}")
    if not raw_result:
        status = r.get(f"status:{job_id}")
        if not status:
            return JSONResponse(status_code=404, content={"error": "Job not found"})
        return JSONResponse(status_code=202, content={"status": status, "message": "Job still in progress"})
 
    result_data = json.loads(raw_result)
    return {"job_id": job_id, **result_data}