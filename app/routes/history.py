from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import get_db
from app.models.calculation import Calculation
from app.routes.user import get_current_user

router = APIRouter(tags=["History & Stats"])


# ✅ GET USER HISTORY
@router.get("/history")
def get_history(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    calculations = db.query(Calculation).filter(
        Calculation.user_id == user.id
    ).all()

    return calculations


# ✅ GET USER STATISTICS
@router.get("/stats")
def get_stats(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    calculations = db.query(Calculation).filter(
        Calculation.user_id == user.id
    ).all()

    total = len(calculations)

    if total == 0:
        return {
            "total_calculations": 0,
            "average_result": 0
        }

    average = sum(calc.result for calc in calculations) / total

    return {
        "total_calculations": total,
        "average_result": average
    }