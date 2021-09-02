from fastapi import  APIRouter ,Depends , status , Response , HTTPException
from practice.database import get_db
from sqlalchemy.orm import  Session
from typing import List
from .. import schemas, models
from ..oauth2 import get_current_user

from ..repository import userRepo


router=APIRouter(prefix="/user",tags=['users'])

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.User,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return userRepo.create(request,db)

@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser])
def get(db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return userRepo.get_all(db)