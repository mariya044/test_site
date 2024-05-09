FROM python:3.10
WORKDIR /PycharmProjects/test_site/test_site
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]