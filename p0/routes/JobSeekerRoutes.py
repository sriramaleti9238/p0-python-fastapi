from fastapi import APIRouter

router=APIRouter()


@router.get("/hi")
def hello():
    return "hello"
