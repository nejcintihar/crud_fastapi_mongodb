from model import Book
from config import database
import uuid
from fastapi import HTTPException


class BookRepo():

    @staticmethod
    async def retrieve():
        try:
            _book = []
            collection = database.get_collection('book').find()
            async for book in collection:
                _book.append(book)
            return _book
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def insert(book: Book):
        try:
            id = str(uuid.uuid4())
            _book = {
                "_id": id,
                "title": book.title,
                "description": book.description
            }
            await database.get_collection('book').insert_one(_book)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def update(id: str, book: Book):
        try:
            _book = await database.get_collection('book').find_one({"_id": id})
            if _book is None:
                raise ValueError(f"Book with id {id} not found")

            _book["title"] = book.title
            _book["description"] = book.description
            await database.get_collection('book').update_one({"_id": id}, {"$set": _book})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def retrieve_id(id: str):
        try:
            return await database.get_collection('book').find_one({"_id": id})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def delete(id: str):
        try:
            await database.get_collection('book').delete_one({"_id": id})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
