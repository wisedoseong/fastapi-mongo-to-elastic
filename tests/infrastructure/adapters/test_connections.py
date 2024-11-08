import pytest
from app.infrastructure.config.database import db
from app.infrastructure.adapters.persistence.mongodb_adapter import MongoDBAdapter
from app.infrastructure.adapters.persistence.elasticsearch_adapter import ElasticsearchAdapter

pytestmark = pytest.mark.asyncio

async def test_mongodb_connection():
    try:
        await db.connect()
        mongo_adapter = MongoDBAdapter("test_db")
        collection = mongo_adapter.get_collection("test")
        
        assert collection is not None
    finally:
        await db.close()

async def test_elasticsearch_connection():
    try:
        await db.connect()
        es_adapter = ElasticsearchAdapter("test") 
        # 헬스체크로 변경
        health = await es_adapter.client.cluster.health()

        assert health['status'] in ['green', 'yellow', 'red']
    finally:
        await db.close()