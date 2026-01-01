FROM alpine:3.23.2

RUN apk update && apk upgrade

RUN apk add uv

WORKDIR /app

COPY . ./

RUN uv sync

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8080

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]

