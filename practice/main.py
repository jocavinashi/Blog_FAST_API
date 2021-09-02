# from fastapi.params import Depends
from typing_extensions import final
from practice import models
from fastapi import FastAPI 
from practice.database import engine
from practice.routers import blog , user , authentication

app=FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)



# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['blogs'])
# async def createblog(request:schemas.Blog,db: Session = Depends(get_db)):
#     new_blog=models.Blog(title=request.title,body=request.body,user_id=request.user_id)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.get('/blog',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowBlog],tags=['blogs'])
# def getblog(db: Session = Depends(get_db)):
#     blogs=db.query(models.Blog).all()
#     return blogs

# @app.get('/blog/{id}',status_code=200,response_model=schemas.ShowBlog,tags=['blogs'])
# def retrieveblog(id,db: Session = Depends(get_db)):
#     blogs=db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
#     return blogs

# @app.delete('/blog/{id}',status_code=status.HTTP_200_OK,tags=['blogs'])
# def destroy(id,db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
#     blog.delete(synchronize_session=False)
#     db.commit()
#     return {"detail":f"blog with id {id} successfully deleted"}

# @app.put('/blog/{id}',status_code=status.HTTP_200_OK,tags=['blogs'])
# def put(id,request:schemas.Blog ,db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with the id {id} is not available')
#     # import pdb;pdb.set_trace()
#     blog.update(request.__dict__)
#     db.commit()
#     return request

# @app.post('/user',status_code=status.HTTP_201_CREATED,tags=['users'])
# def create_user(request:schemas.User,db: Session = Depends(get_db)):
#     new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user',status_code=status.HTTP_200_OK,response_model=List[schemas.ShowUser],tags=['users'])
# def getuser(db: Session = Depends(get_db)):
#     user=db.query(models.User).all()
#     return user





