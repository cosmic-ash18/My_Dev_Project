FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache django
RUN python manage.py makemigrations
RUN python manage.py migrate
EXPOSE 0000

ENV DJANGO_SETTINGS_MODULE=oj_project.settings
ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]