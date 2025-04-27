# using python as base image which will already have uv installed 
FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

# set the working directory
WORKDIR /app

# copy all source code to the working directory along with pyproject.toml 
COPY . .
RUN uv pip install -r pyproject.toml --system

CMD [ "python3", "/app/main.py" ]