1. Execute uvicron server via local machine:
$ cd %PATH%/test_task
$ uvicorn app.main:app --reload



OPTIONAL:

2. Pytest
$ cd %path%/test_task
$ pytest


3. Docker
$ cd %PATH%/test_task
$ docker build -t test_task_image .
$ docker run -h "127.0.0.1" -d --name test_task_container -p 8000:8000 test_task_image

After successfull load try this:
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/api/v1/devices
