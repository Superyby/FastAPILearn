from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["user"])

@router.get("/list")
async  def get_users():
    return ["user1", "user2", "user3"]