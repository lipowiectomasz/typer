FROM python:3

WORKDIR /usr/src/app

COPY ./pythonback/requirements.txt ./
RUN pip install --no-cache-dir -r ./pythonback/requirements.txt

COPY . .

EXPOSE 8000

