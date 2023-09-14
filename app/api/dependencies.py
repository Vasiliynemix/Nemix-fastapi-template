from typing import Annotated

from fastapi import Depends

from app.utils.unitofwork import UnitOfWork, IUnitOfWork

UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]
