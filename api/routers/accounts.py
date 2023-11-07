from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)

from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel
from typing import List
from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountRepository,
    DuplicateAccountError,
    AccountInTest,
)


class AccountForm(BaseModel):
    email: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/accounts/all/", response_model=List[AccountOut])
def get_all_accounts(
    repo: AccountRepository = Depends(),
):
    return repo.get_all_accounts()


@router.get("/api/protected", response_model=bool)
async def get_protected(
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return True


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.post("/api/accounts", response_model=AccountToken | HttpError)
async def create_account(
    info: AccountInTest,
    request: Request,
    response: Response,
    accounts: AccountRepository = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account_in = AccountIn(
            email=info.email,
            password=info.password
        )
        account = accounts.create(account_in, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(email=info.email, password=info.password)
    token = await authenticator.login(response, request, form, accounts)

    return AccountToken(account=account, **token.dict())
