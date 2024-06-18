from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import ENGINE, session
from models import Testominal, User
from fastapi.encoders import jsonable_encoder
from schemas import ClientCommentM
from fastapi_jwt_auth import AuthJWT
from typing import List

# Initialize the session with the database engine
session = session(bind=ENGINE)
clientcomments_router = APIRouter(prefix="/testominal")


@clientcomments_router.get("/", response_model=List[ClientCommentM])
def get_comments(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    comments = session.query(Testominal).all()
    context = [
        {
            "id": comment.id,
            "msg": comment.msg,
            "full_name": comment.full_name
        }
        for comment in comments
    ]
    return jsonable_encoder(context)


@clientcomments_router.post("/create", status_code=status.HTTP_201_CREATED)
def create_comment(comment: ClientCommentM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    new_comment = Testominal(
        content=comment.content,
        client_id=exist_user.id
    )

    session.add(new_comment)
    session.commit()

    context = {
        "status_code": status.HTTP_201_CREATED,
        "msg": "Comment created",
        "data": {
            "id": comment.id,
            "msg": comment.msg,
            "full_name": comment.full_name
        }
    }
    return context


@clientcomments_router.get("/{id}", response_model=ClientCommentM)
async def get_comment(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    check_comment = session.query(Testominal).filter(Testominal.id == id).first()
    if check_comment:
        context = {
            "id": check_comment.id,
            "msg": check_comment.msg,
            "full_name": check_comment.full_name
        }
        return jsonable_encoder(context)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@clientcomments_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_comment(id: int, data: ClientCommentM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    comment = session.query(Testominal).filter(Testominal.id == id).first()
    if comment:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(comment, key, value)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Comment updated"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")


@clientcomments_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_comment(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    comment = session.query(Testominal).filter(Testominal.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    session.delete(comment)
    session.commit()

    context = {
        "status_code": 200,
        "msg": "Comment deleted"
    }
    return jsonable_encoder(context)
