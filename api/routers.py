import json
from uuid import uuid4

from fastapi import APIRouter

from api.redis_setup import redis_plug
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

    redis_plug.lpush("job_queue", json.dumps(job_stats))
    
    redis_plug.set(f'status:{job_id}', 'queued')
    
    return {'job_id': job_id, 'status': 'queued'}


@router.get('/status/{job_id}')
def get_status(job_id: str):
    status = redis_plug.get(f'status:{job_id}')
    if status:
        return {'job_id': job_id, 'status': status}
    
    return {'error': 'Job not found'}