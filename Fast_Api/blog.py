from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import ENGINE, session
from models import Blog, User
from fastapi.encoders import jsonable_encoder
from schemas import BlogM
from fastapi_jwt_auth import AuthJWT
from typing import List

# Initialize the session with the database engine
session = session(bind=ENGINE)
blog_router = APIRouter(prefix="/blog")


@blog_router.get("/", response_model=List[BlogM])
def get_blogs(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    blogs = session.query(Blog).all()
    context = [
        {
            "id": blog.id,
            "title": blog.title,
            "owner": blog.owner,
            
            "slug": blog.slug,
            
        }
        for blog in blogs
    ]
    return jsonable_encoder(context)


@blog_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        new_blog = Blog(
            title=blog.title,
            owner=blog.owner,
            
            slug=blog.slug
        )

        session.add(new_blog)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Blog created",
            "data": {
                "id": new_blog.id,
                "title": new_blog.title,
                "owner": new_blog.owner,
                
                "slug": new_blog.slug,
                
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to create blog")


@blog_router.get("/{id}", response_model=BlogM)
async def get_blog(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    check_blog = session.query(Blog).filter(Blog.id == id).first()
    if check_blog:
        context = {
            "id": check_blog.id,
            "title": check_blog.title,
            "owner": check_blog.owner,
            
            "slug": check_blog.slug,
           
        }
        return jsonable_encoder(context)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")


@blog_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_blog(id: int, data: BlogM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        blog = session.query(Blog).filter(Blog.id == id).first()
        if blog:
            for key, value in data.dict(exclude_unset=True).items():
                setattr(blog, key, value)
            session.commit()

            context = {
                "status_code": 200,
                "msg": "Blog updated"
            }
            return jsonable_encoder(context)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to update blog")


@blog_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_blog(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        blog = session.query(Blog).filter(Blog.id == id).first()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

        session.delete(blog)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Blog deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to delete blog")
