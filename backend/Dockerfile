FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml /app/
RUN pip install --no-cache-dir -U pip && \
pip install --no-cache-dir -r <(python - <<'PY'\nfrom tomllib import loads\nprint('\n'.join(loads(open('pyproject.toml','rb').read()).get('project',{}).get('dependencies',[])))\nPY
)
COPY app /app/app
ENV PYTHONUNBUFFERED=1
CMD ["uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]