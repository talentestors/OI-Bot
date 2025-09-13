FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --frozen --link-mode=copy

COPY . /app

# Create log directory
RUN mkdir -p log

RUN [ -f .env ] || cp .env.example .env

# Make start script executable
RUN chmod +x start-bot.sh

EXPOSE 8024

CMD ["./start-bot.sh"]
