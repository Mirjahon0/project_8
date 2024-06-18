from fastapi import APIRouter, HTTPException, status, Depends
from database import ENGINE, session
from models import Chairs, User
from fastapi.encoders import jsonable_encoder
from schemas import ProductM
from fastapi_jwt_auth import AuthJWT


session = session(bind=ENGINE)
chairs_router = APIRouter(prefix="/chairs")


@chairs_router.get("/")
def get_chairs(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    chaires = session.query(Chairs).all()
    context = [
        {
            "id": chairs.id,
            "name": chairs.name,
            "description": chairs.description,
            "price": chairs.price,
            "prices": chairs.prices,
            "slug": chairs.slug,
            "image": chairs.image
        }
        for chairs in chaires
    ]

    return jsonable_encoder(context)


@chairs_router.post("/create")
def create_chairs(product: ProductM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

    exist_user = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")

    if exist_user.is_staff:
        chairs = Chairs(
            name=product.name,
            description=product.description,
            price=product.price,
            
            prices=product.prices,
            slug=product.slug,
            image=product.image
        )

        session.add(chairs)
        session.commit()

        context = {
            "status_code": status.HTTP_201_CREATED,
            "msg": "Product created",
            "data": {
                "id": chairs.id,
                "name": chairs.name,
                "description": chairs.description,
                "price": chairs.price,
                "prices": chairs.prices,
                "slug": chairs.slug,
                "image": chairs.image
            }
        }
        return context
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not authorized to create product")


@chairs_router.get("/{id}")
async def get_product(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    check_chairs = session.query(Chairs).filter(Chairs.id == id).first()
    if check_chairs:
        context = [
            {
                "id": check_chairs.id,
                "name": check_chairs.name,
                "description": check_chairs.description,
                "price": check_chairs.price,
                "prices": check_chairs.prices,
                "slug": check_chairs.slug,
                "image": check_chairs.image
            }
        ]
        return jsonable_encoder(context)
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="product not found")


@chairs_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_product(id: int, data: ProductM, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        product = session.query(Chairs).filter(Chairs.id == id).first()
        if product:

            for key, value in data.dict(exclude_unset=True).items():
                setattr(product, key, value)

            session.commit()
            context = {
                    "status_code": 200,
                    "msg": "Product updated"
                }
            return jsonable_encoder(context)
        else:
            return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Failed!")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to update product data for you")


@chairs_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_product(id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")
    exist_users = session.query(User).filter(User.username == Authorize.get_jwt_subject()).first()
    if not exist_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The user does not exist")
    if exist_users.is_staff:
        product = session.query(Chairs).filter(Chairs.id == id).first()
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

        session.delete(product)
        session.commit()

        context = {
            "status_code": 200,
            "msg": "Product deleted"
        }
        return jsonable_encoder(context)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not possible to delete product data for you")
