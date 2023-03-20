FROM python:3.9
WORKDIR /evilcats-api
COPY ./requirements.txt /evilcats-api/requirements.txt
COPY ./evilcats-api .
RUN pip install -r /evilcats-api/requirements.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
EXPOSE 8000
#RUN python3 -m uvicorn main:app --reload
#docker build --pull --rm -f "Dockerfile" -t evilcats:latest "."