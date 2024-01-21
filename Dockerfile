FROM python:3.10
RUN groupadd -r docker && useradd -r -g docker docker
RUN apt-get update && apt-get install -y \
    gettext \
    libpcre3 \
    libpcre3-dev \
    rsync
#    --no-install-recommends && rm -rf /var/lib/apt/lists/* \

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99
RUN mkdir -p /code
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
#COPY ./migrations /code
#COPY alembic.ini /code
#COPY ./app /code/app
WORKDIR /code
#CMD ["uvicorn", "app.main:app", "--reload",  "--host", "0.0.0.0", "--port", "8000"]
