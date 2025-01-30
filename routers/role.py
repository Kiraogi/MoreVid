from fastapi import APIRouter, HTTPException
from models import User
from database import users_collection

router = APIRouter()

@router.get("/restricted-resource")
def get_restricted_resource(user: User = Depends(get_current_user)):
    # Check the user's role and return the restricted resource if they have the required access level
    if user.role == "admin":
        return {"message": "Welcome to the restricted resource"}
    else:
        raise HTTPException(status_code=403, detail="Forbidden")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # Check the token and return the current user if it is valid
    credentials_exception = HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")
    try:
        payload = oauth2_scheme.decode_token(token)
        user_id = payload.get("sub")
        user = users_collection.find_one({"_id": user_id})
        if user:
            return user
        else:
            raise credentials_exception
    except JWTError:
        raise credentials_exception