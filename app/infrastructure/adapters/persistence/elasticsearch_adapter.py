from typing import Any, Dict, List, Optional
from elasticsearch import AsyncElasticsearch
from app.infrastructure.config.database import db

class ElasticsearchAdapter:
    def __init__(self, index_name: str):
        """
        index_name: Elasticsearch 인덱스 이름
        """
        self.index_name = index_name
    
    @property
    def client(self) -> AsyncElasticsearch:
        """Elasticsearch 클라이언트 반환"""
        return db.elasticsearch_client
    
    def get_index(self) -> str:
        """인덱스 이름 반환"""
        return self.index_name

# 사용 예시:
"""
adapter = ElasticsearchAdapter("your_index")
client = adapter.client

# Elasticsearch의 내장 메서드를 직접 사용
await client.search(
    index=adapter.get_index(),
    body={"query": {"match": {"field": "value"}}}
)

await client.index(
    index=adapter.get_index(),
    body={"field": "value"}
)

await client.update(
    index=adapter.get_index(),
    id="doc_id",
    body={"doc": {"field": "new_value"}}
)

await client.delete(
    index=adapter.get_index(),
    id="doc_id"
)
"""