from sqlalchemy.orm import Session
from practice import models, schemas
from fastapi import HTTPException ,status

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail":f"blog with id {id} successfully deleted"}

def update(request:schemas.Blog,id:int,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
    # import pdb;pdb.set_trace()
    blog.update(request.__dict__)
    db.commit()
    return request

def retrieve(id:int,db:Session):
    blogs=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
    return blogs