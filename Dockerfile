# Gunakan image dasar
FROM python:3.12-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.7.7 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

# Set workdir
WORKDIR /app

# Salin kode & dependensi
COPY app/ /app
COPY models/ /app/models
COPY app/requirements.txt .

# Install dependencies langsung ke sistem (tanpa virtualenv)
# RUN pip install --no-cache-dir -r requirements.txt

# Install the requirements using uv
RUN uv pip install -r requirements.txt

EXPOSE 5000

# Create a non-root user and switch to it
RUN useradd -m app_user
USER app_user

# Jalankan aplikasi
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]