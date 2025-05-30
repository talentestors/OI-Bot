FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Create non-privileged user
RUN groupadd --gid 1000 oi-bot && \
    useradd --uid 1000 --gid oi-bot --shell /bin/bash --create-home oi-bot

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --no-dev --link-mode=hardlink

COPY . /app

# Create log directory and set permissions
RUN mkdir -p log && \
    chown -R oi-bot:oi-bot /app

# Create and set permissions for nonebot2 plugin directories and home directory
RUN mkdir -p /home/oi-bot && \
    chown -R oi-bot:oi-bot /home/oi-bot && \
    chmod -R 755 /home/oi-bot

RUN [ -f .env ] || cp .env.example .env

# Make start script executable
RUN chmod +x start-bot.sh

# Switch to non-privileged user
USER oi-bot

EXPOSE 8024

CMD ["./start-bot.sh"]
