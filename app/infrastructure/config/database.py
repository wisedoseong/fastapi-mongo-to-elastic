from motor.motor_asyncio import AsyncIOMotorClient
from elasticsearch import AsyncElasticsearch
from ..config.setting import settings

class Database:
    def __init__(self):
        self.mongodb_client: AsyncIOMotorClient = None
        self.elasticsearch_client: AsyncElasticsearch = None
    
    async def connect(self):
        # MongoDB 연결
        self.mongodb_client = AsyncIOMotorClient(settings.MONGODB_URI)
        
        #Elasticsearch 연결
        self.elasticsearch_client = AsyncElasticsearch(
            settings.ELASTICSEARCH_PATH,
            api_key=settings.ELASTICSEARCH_API_KEY,
            request_timeout=60,
            retry_on_timeout=True,
            max_retries=3
        )
    
    async def close(self):
        # 연결 종료
        if self.mongodb_client:
            self.mongodb_client.close()
        if self.elasticsearch_client:
            await self.elasticsearch_client.close()

# 전역 데이터베이스 인스턴스
db = Database()