from pip._internal.utils.appdirs import user_cache_dir

from database.db import Session
from model.schema import JobDetails
from model.DataModels import JobModel

def create_job(application :JobModel):
    db = Session()
    job_details = JobDetails(
        compName=application.compName,
        jobExperience=application.jobExperience,
        jobRole=application.jobRole,
        techStack=application.techStack,
        location=application.location,
        salary=application.salary,
        dateOfApplication=application.dateOfApplication,
        user_id=application.userId
    )
    db.add(job_details)
    db.commit()
    db.close()
    return job_details