from fastapi import APIRouter

router = APIRouter()


@router.get("/tbpl")
async def get_user_details() -> str:
    return "Hello"