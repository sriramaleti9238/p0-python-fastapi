from fastapi import APIRouter
from model.DataModels import JobModel
from services.JobPostingService import create_job

emp_router=APIRouter()


@emp_router.post("/postjob")
def post_job(job : JobModel):
    job_details= create_job(job)
    if job_details is not None:
        return {"data": job_details, "message": "Job posted successfully"}
    return "details not posted into db"
