FROM python:3.7.5

WORKDIR /app
COPY . .
RUN pip install flask
RUN python -m pip install -r requirements.txt
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD flask run
