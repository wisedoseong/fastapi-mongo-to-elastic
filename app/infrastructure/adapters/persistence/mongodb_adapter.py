from typing import Any, Dict, List, Optional, Type
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from app.infrastructure.config.database import db

class MongoDBAdapter:
    def __init__(self, database_name: str):
        """
        database_name: MongoDB 데이터베이스 이름
        """
        self.database_name = database_name
    
    @property
    def database(self):
        """데이터베이스 객체 반환"""
        return db.mongodb_client[self.database_name]
    
    def get_collection(self, collection_name: str) -> AsyncIOMotorCollection:
        """Motor 컬렉션 객체를 직접 반환"""
        return self.database[collection_name]

# 사용 예시:
"""
adapter = MongoDBAdapter("your_db")
collection = adapter.get_collection("your_collection")

# Motor의 내장 메서드를 직접 사용
await collection.find_one({"field": "value"})
await collection.insert_one({"field": "value"})
await collection.update_many(query, update)
await collection.aggregate(pipeline)
"""