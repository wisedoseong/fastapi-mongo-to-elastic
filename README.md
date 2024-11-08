# MongoDB to Elasticsearch Migration Project

헥사고날 아키텍처를 적용한 MongoDB에서 Elasticsearch로의 데이터 이관 프로젝트입니다.

## 기술 스택
- Python 3.12+
- FastAPI
- MongoDB
- Elasticsearch
- Poetry (의존성 관리)
- Hexagonal Architecture

## 설치 및 실행

### Prerequisites
- Python 3.9 이상
- Poetry

### Poetry 설치
```bash
# Windows
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# macOS, Linux
curl -sSL https://install.python-poetry.org | python3 -
```

### 프로젝트 설치

```bash
# 프로젝트 클론
git clone [repository-url]
cd [project-directory]

# Poetry를 통한 의존성 설치
poetry install

# 가상환경 진입
poetry shell

# 서버 실행
poetry run uvicorn main:app --reload
```

### 환경 변수 설정

.env 파일을 프로젝트 루트에 생성하고 다음 변수들을 설정하세요:
```bash
MONGODB_URI=mongodb://localhost:27017
ELASTICSEARCH_URL=http://localhost:9200
```

### 의존성 관리

```bash
# 새로운 패키지 추가
poetry add [package-name]

# 개발 의존성 추가
poetry add --dev [package-name]

# 의존성 업데이트
poetry update
```

## 아키텍처

이 프로젝트는 헥사고날 아키텍처를 따르며 다음과 같은 레이어로 구성되어 있습니다:

- Domain: 비즈니스 엔티티와 규칙
- Application: 유스케이스와 포트 정의
- Infrastructure: 외부 시스템 어댑터 구현
- Presentation: API 엔드포인트와 스키마

## 프로젝트 구조

```bash
├── app/
│   ├── domain/                    # 도메인 계층
│   │   ├── common/                # 공통 모듈
│   │   └── product/               # 제품 관련 도메인
│   │
│   ├── application/               # 애플리케이션 계층
│   │   ├── ports/                 # 포트 인터페이스
│   │   ├── services/              # 서비스 구현
│   │   └── usecases/              # 유스케이스 정의 및 구현
│   │
│   ├── infrastructure/            # 인프라스트럭처 계층
│   │   ├── config/                # 설정
│   │   ├── adapters/              # 외부 시스템 어댑터
│   │   └── repositories/          # 저장소 구현체
│   │
│   ├── presentation/              # 프레젠테이션 계층
│   │   ├── api/                   # API 라우터
│   │   ├── schemas/               # 요청/응답 스키마
│   │   └── middlewares/           # 미들웨어
│   │
│   └── utils/                     # 유틸리티
│
├── tests/                         # 테스트 코드
├── pyproject.toml                 # Poetry 프로젝트 설정
├── poetry.lock                    # Poetry 의존성 잠금 파일
└── main.py                        # 애플리케이션 엔트리포인트
```

## API 문서

서버 실행 후 다음 URL에서 API 문서를 확인할 수 있습니다:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 테스트 실행

```bash
# 테스트 실행
pytest
```

## 라이센스

MIT License

## 기여

이슈와 풀 리퀘스트를 환영합니다.