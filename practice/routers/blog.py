from fastapi import  APIRouter ,Depends , status , Response , HTTPException
from practice.database import get_db
from sqlalchemy.orm import  Session
from typing import List
from .. import schemas, models
from ..oauth2 import get_current_user

from ..repository import blogRepo

router=APIRouter(prefix="/blog",tags=['blogs'])


@router.post('/',status_code=status.HTTP_201_CREATED)
async def create(request:schemas.Blog,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepo.create(request,db)
    
@router.get('/',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog])
def get(db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepo.get_all(db)

@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def retrieve(id,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepo.retrieve(id,db)

@router.delete('/{id}',status_code=status.HTTP_200_OK)
def destroy(id,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepo.delete(id,db)
    
@router.put('/{id}',status_code=status.HTTP_200_OK)
def put(id,request:schemas.Blog ,db: Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepo.update(request,id,db)