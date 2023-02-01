FROM python:3.10.5-alpine

RUN mkdir /home/app
WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

RUN apk update \ 
    && apk add gcc python3-dev musl-dev 

RUN pip install --upgrade pip
COPY ./requirements.txt . 
RUN pip install -r requirements.txt 


#criando pasta de arquivos static
RUN mkdir /home/app/static

COPY . . 

EXPOSE 8000

COPY entrypoint.sh . 
RUN chmod +x ./entrypoint.sh

#CMD [ "python", "manage.py", "collectstatic", "--no-input" ]
#CMD [ "python", "manage.py", "flush", "--no-input" ]
ENTRYPOINT [ "./entrypoint.sh" ]

