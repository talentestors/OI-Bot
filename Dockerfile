FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

COPY . /app

RUN [ -f .env ] || cp .env.example .env

EXPOSE 8024

CMD ["uv", "run", "bot.py"]
