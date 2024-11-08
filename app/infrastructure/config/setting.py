from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    MONGODB_URI: str 
    ELASTICSEARCH_PATH: str # .env 파일에 ELASTICSEARCH_URI 로 설정하면 localhost:9200 로 호출됨
    ELASTICSEARCH_API_KEY: str
    
    model_config = ConfigDict(
        env_file = '.env',
        env_file_encoding = 'utf-8'
    )

settings = Settings()