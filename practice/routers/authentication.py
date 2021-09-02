from fastapi.security import OAuth2PasswordRequestForm
from practice import  schemas ,models
from practice.database import get_db
from fastapi import APIRouter ,Depends , HTTPException ,status
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..token import create_access_token

router=APIRouter(tags=['auth'])


@router.post('/login')
async def login(request:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Invalid username')
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Incorrect password')
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}