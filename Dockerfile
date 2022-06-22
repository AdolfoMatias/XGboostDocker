FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app/

COPY main.py requirements.txt .flaskenv  model.pkl /app/  
COPY static /app/static
COPY templates /app/templates
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 3000/tcp
CMD ["python","main.py"]