from fastapi import APIRouter
from views import tcc, tbpl
router = APIRouter()

router.include_router(tcc.router, tags=["TCC"])
router.include_router(tbpl.router, tags=["TBPL"])