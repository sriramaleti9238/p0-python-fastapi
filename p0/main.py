from fastapi import FastAPI
from routes.JobSeekerRoutes import router
from routes.RegisterLoginRoutes import user_router
from routes.EmployeeRoutes import emp_router

app=FastAPI()

app.include_router(router ,prefix="/api")
app.include_router(user_router ,prefix="/user")
app.include_router(emp_router,prefix="/emp")