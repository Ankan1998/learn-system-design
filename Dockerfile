# ---------- Stage 1: build the static site ----------
FROM python:3.12-slim AS builder

WORKDIR /build

# Install docs toolchain first so this layer caches across content edits.
COPY requirements-docs.txt ./
RUN pip install --no-cache-dir -r requirements-docs.txt

COPY . .

# Flatten the curriculum into docs/ (rewriting links), then render to site/.
RUN python scripts/build_docs.py && mkdocs build

# ---------- Stage 2: serve ----------
FROM nginx:1.27-alpine AS runtime

COPY --from=builder /build/site /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

# Use 127.0.0.1, not "localhost": that resolves to ::1 first in this image.
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1/ >/dev/null 2>&1 || exit 1

CMD ["nginx", "-g", "daemon off;"]
