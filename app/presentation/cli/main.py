import click
from app.infrastructure.config.database import db
#from app.application.usecases.implementations.migration_service import MigrationService

@click.group()
def cli():
    """MongoDB to Elasticsearch 마이그레이션 도구"""
    pass

# @cli.command()
# @click.option('--batch-size', default=1000, help='한 번에 처리할 문서 수')
# def migrate(batch_size):
#     """MongoDB 데이터를 Elasticsearch로 마이그레이션"""
#     migration_service = MigrationService(db)
#     migration_service.migrate_data(batch_size)

# @cli.command()
# def sync():
#     """실시간 데이터 동기화 시작"""
#     migration_service = MigrationService(db)
#     migration_service.start_sync()

if __name__ == '__main__':
    cli()
    
    
# 사용 예시:
"""
poetry run cli-tool migrate --batch-size 1000
poetry run cli-tool sync
"""