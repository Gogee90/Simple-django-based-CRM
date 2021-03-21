# In path/to/your/dev/folder/Dockerfile
# Base Image
FROM python:3
ENV PYTHONBUFFERED=1
WORKDIR /Simple-django-based-CRM
COPY requirements.txt /Simple-django-based-CRM/
RUN pip install -r requirements.txt
COPY . /Simple-django-based-CRM/