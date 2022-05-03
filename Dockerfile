# Dockerfile, Image, Container
FROM python:3.9

ADD krypin_v01.py .

CMD ["python", "krypin_v01.py"]0