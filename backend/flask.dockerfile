FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt ./

#RUN pip install -r requirements.txt
# Install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    pip install -r requirements.txt && \
    apt-get remove -y gcc && \
    apt-get autoremove -y

COPY . .

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000" ]