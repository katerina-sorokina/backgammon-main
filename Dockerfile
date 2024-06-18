FROM python:3.12-slim AS builder

WORKDIR /backgammon

COPY requirements.txt .

RUN pip install --user -r requirements.txt



FROM python:3.12-slim AS runtime

COPY --from=builder /root/.local /root/.local

WORKDIR /backgammon

COPY . .

ENV PATH=/root/.local/bin:$PATH

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
