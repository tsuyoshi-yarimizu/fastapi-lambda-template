from fastapi import APIRouter
from typing import Dict
from src.utils.custom_logger import custom_logger as log

router = APIRouter()


@router.get('/')
def health_check(param1: str = None) -> Dict:
    log.info(param1)
    return {
        "message": "I'm fine."
    }
