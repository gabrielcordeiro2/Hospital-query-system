FROM python:3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD python ./src/api/app.py
