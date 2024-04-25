from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base ,engine



from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))
    user_type = Column(String(10))  # 'jobseeker' or 'employer'

    posted_jobs = relationship("Job", back_populates="posted_by")
    applications = relationship("Job", secondary="job_applications", back_populates="applicants")

class JobDetails(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    compName = Column(String(50))
    jobExperience = Column(String(50))
    jobRole = Column(String(50))
    techStack = Column(String(50))
    location = Column(String(50))
    salary = Column(Integer)
    dateOfApplication = Column(DateTime)
    posted_by_id = Column(Integer, ForeignKey('users.id'))

    posted_by = relationship("User", back_populates="posted_jobs")
    applicants = relationship("User", secondary="job_applications", back_populates="applications")

class JobApplication(Base):
    __tablename__ = 'job_applications'

    id = Column(Integer, primary_key=True, autoincrement=True)
    job_id = Column(Integer, ForeignKey('jobs.id'))
    jobseeker_id = Column(Integer, ForeignKey('users.id'))

    job = relationship("Job")
    jobseeker = relationship("User")

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
