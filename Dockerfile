FROM ghcr.io/astral-sh/uv:latest

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev

COPY . /app

RUN [ -f .env ] || cp .env.example .env

EXPOSE 8024

CMD ["uv", "run", "bot.py"]
