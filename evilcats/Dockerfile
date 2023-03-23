FROM python:3.9
WORKDIR /evilcats/
COPY ./requirements.txt ./requirements.txt
COPY ./evilcats-api ./
RUN pip install -r ./requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 8000
#docker build --pull --rm -f "Dockerfile" -t evilcats:latest "."
#docker run -d --name evilcats_container -p 8000:80 evilcats