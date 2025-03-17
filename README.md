<p align="center">
  <a href="https://github.com/AlexDemure/fastgenerator">
    <a href="https://ibb.co/TBZ0V6N6"><img src="https://i.ibb.co/N6XN85G5/fastgenerator.png" alt="fastgenerator" border="0" /></a>
  </a>
</p>

<p align="center">
  CLI-утилита для кодогенерации на основе YAML-файла.
</p>

---

### Установка
```pip install fastgenerator```

### Использование
Основные команды
1. Создание структуры проекта:

```fastgenerator create app -f {файл-конфигурация.yaml}```

2. Добавление модуля в проект:

```fastgenerator add module {название модуля} -f {файл-конфигурация.yaml}```

### Примеры кодогенерации на основе yaml-файлов
```templates/example.yaml``` 
```
app:
  tree:
    src: {}
    tests: {}
  files:
    - path: "src/endpoints.py"
      content: |
        from fastapi import APIRouter
        from fastapi import Path
        from fastapi import status
  
        router = APIRouter()
    - path: "src/application.py"
      content: |
        from contextlib import asynccontextmanager
  
        import uvicorn
        from fastapi import FastAPI
        from fastapi.middleware.cors import CORSMiddleware
        from fastapi.openapi.docs import get_redoc_html
        from fastapi.openapi.docs import get_swagger_ui_html
        from fastapi.openapi.utils import get_openapi
        from endpoints import router
  
        @asynccontextmanager
        async def lifespan(_: FastAPI):
            yield
  
  
        app = FastAPI(
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
        )
  
  
        @app.get(
            "/docs",
            include_in_schema=False,
        )
        async def swagger():
            return get_swagger_ui_html(openapi_url="/openapi.json", title=app.title)
  
  
        @app.get(
            "/redoc",
            include_in_schema=False,
        )
        async def redoc():
            return get_redoc_html(openapi_url="/openapi.json", title=app.title)
  
  
        @app.get(
            "/openapi.json",
            include_in_schema=False,
        )
        async def openapi():
            return get_openapi(title=app.title, version=app.version, routes=app.routes)
  
  
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
  
        app.include_router(router)
  
        if __name__ == '__main__':
            uvicorn.run(
                "src.application:app",
                port=8000,
                host="0.0.0.0",
                app_dir="src",
            )
    - path: "src/settings.py"
      content: |
        from enum import StrEnum
        from enum import auto
  
        from pydantic_settings import SettingsConfigDict
  
  
        class Env(StrEnum):
            develop = auto()
            production = auto()
  
  
        configs = []
  
  
        class Settings(*configs):  # type:ignore
            model_config = SettingsConfigDict(env_file=".env", case_sensitive=True, extra="ignore")
            ENV: Env
  
  
        settings = Settings()
    - path: "ruff.toml"
      content: |
        exclude = [
          ".ruff_cache",
          ".venv",
          ".git",
          "__pycache__",
          ".pytest_cache",
          ".mypy_cache",
          "pyproject.toml"
        ]
        include = ["*.py"]
        respect-gitignore = true
        show-fixes = true
        line-length = 120
        indent-width = 4
        target-version = "py310"
    - path: "format.sh"
      content: |
        ruff format src/ --no-cache

module:
  files:
    - path: "src/endpoints.py"
      content: |
        @router.get(
          "/${kebab}:{id:int}",
          status_code=status.HTTP_200_OK,
          response_model=dict,
        )
        async def get_${snake}(${snake}_id: int = Path(..., ge=1, alias="id")) -> dict:
            return dict(id=${snake}_id)

uv:
  main:
    - fastapi
    - uvicorn
    - pydantic
    - pydantic-settings
    - python-multipart
  lints:
    - ruff
```
```templates/application.yaml``` - Более комплексная конфигурация на стеке FastAPI, SQLAlchemy, Pydantic, Alembic, PostgreSQL, Isort, Ruff, Pytest
