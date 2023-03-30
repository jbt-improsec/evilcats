# Evilcats

## Description 
The API that recivces pictures send from the catapp android application. The pictures can be viewed it the [serverIP]:[serverPort]/catpic path. The API runs using python [FastAPI](https://fastapi.tiangolo.com/) and [Uvicorn](https://www.uvicorn.org/)

## Prerequisites 
- Dokcer installed on host machine
- Running it without docker is also possible. In this case:
  - Python installed on host machine.
  - Install all pip packages in requirment.txt file

## Installation 
### Docker
- Go to directory: ./evilcats/evilcats/ 
- Run docker commads to build image and run the container
```
docker build --pull --rm -f "Dockerfile" -t evilcats:latest "."
docker run -d --name evilcats_container -p 8000:80 evilcats
```
- The API should now be running on the host machine port 8000.

### Without Docker
- Go to directory ./evilcats/evilcats/evilcats-api
- Run command:
```
python -m uvicorn main:app --reload --host [host-ip] --port [port]
```
- The API should now be running on the host machine.

## Usage
The api will accept POST request at [hostIP]:8000/catpics/addpics/ and display them in [hostIP]:8000/catpic

