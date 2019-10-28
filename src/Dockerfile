FROM python:3.6.4-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
COPY . .
ENTRYPOINT ["/usr/local/bin/flask"]
CMD ["run", "--host", "0.0.0.0"]
