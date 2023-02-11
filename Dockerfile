FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

WORKDIR /code
COPY . /code

# EXPOSE 8080
#
# # ENTRYPOINT ["python", "manage.py"]
# # CMD ["runsever", "0.0.0.0:8080"]