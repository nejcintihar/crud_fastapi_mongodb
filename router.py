from fastapi import APIRouter
from repository import BookRepo
from model import Book, Response

router = APIRouter()


@router.get("/book/")
async def get_all():
    _bookList = await BookRepo.retrieve()
    return Response(code="200", status="Ok", message="Successfully retrieve all data", result=_bookList).model_dump(exclude_none=True)


@router.post("/book/create")
async def create(book: Book):
    await BookRepo.insert(book)
    return Response(code="200", status="Ok", message="Successfully saved data").model_dump(exclude_none=True)


@router.get("/book/{id}")
async def get_id(id: str):
    _book = await BookRepo.retrieve_id(id)
    return Response(code="200", status="Ok", message="Successfully retrieved data", result=_book).model_dump(exclude_none=True)


@router.put("/book/{id}")
async def update(id: str, book: Book):
    await BookRepo.update(id, book)
    return Response(code="200", status="Ok", message="Successfully updated data").model_dump(exclude_none=True)


@router.delete("/book/{id}")
async def delete(id: str):
    await BookRepo.delete(id)
    return Response(code="200", status="Ok", message="Successfully delete data").dict(exclude_none=True)
