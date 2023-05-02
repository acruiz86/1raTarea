
FROM python:3-alpine

WORKDIR /home/app

COPY requirements.txt ./
RUN pip install --upgrade pip
ENV PIP_ROOT_USER_ACTION=ignore
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "/home/app/run.py"]
