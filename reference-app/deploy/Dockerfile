# Optional container for the reorder page. Last checked: 2026-09-26.
#
# You do not need this on a managed platform that runs Python apps directly.
# It is here for platforms that want a container, and for founders who need to
# run it somewhere a managed platform cannot (cost, privacy, portability).
#
# Build from the reference-app folder:
#   docker build -f deploy/Dockerfile -t copper-pot-reorder .
#
# One stage is enough: nothing is compiled, so a separate build stage would
# only add lines. The base image is pinned to a digest, because a tag can move.

FROM python:3.12-slim@sha256:f77ac9e44ae96ef2c90b8053ea08c31f8be030f824196b0ae4db6d462c84e51f

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    COPPER_POT_DB=/data/copper_pot.db

WORKDIR /srv

# Dependencies first, so a code change does not reinstall them.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY facts ./facts

# Run as a user that cannot change the code. /data holds the SQLite file;
# mount a persistent volume there, or the orders vanish with the container.
RUN useradd --system --uid 10001 --no-create-home app \
    && mkdir /data && chown app /data
USER app

EXPOSE 8000

# The platform's "Up" watch (Chapter 9). Uses Python, since the slim image has no curl.
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/healthz', timeout=3)"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
