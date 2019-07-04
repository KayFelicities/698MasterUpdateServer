FROM python:alpine
LABEL author="Kay"

COPY src /src/
WORKDIR /src
RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python", "/src/app.py"]