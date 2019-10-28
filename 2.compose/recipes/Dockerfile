FROM python:3.6.4-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt && \
    apk update && \
    apk add --no-cache curl && \
    rm -rf /var/cache/apk/*
ENV FLASK_APP=recipe.py
ENV FLASK_ENV=production
COPY src .
ENTRYPOINT ["/usr/local/bin/flask"]
CMD ["run", "--host", "0.0.0.0"]
