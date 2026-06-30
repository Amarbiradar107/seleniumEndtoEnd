FROM python:3.13-slim AS builder

COPY requirements.txt .

RUN pip install --prefix=/install -r requirements.txt

FROM python:3.13-slim

COPY --from=builder /install /usr/local

COPY . .

CMD ["pytest"]