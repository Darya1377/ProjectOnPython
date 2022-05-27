FROM python:3.10.4

WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND=noninteractive
COPY requirements.txt ./
RUN pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt \
    &&apt-get update && apt-get install -y \

        python3-dev \
        python3-pip \
        xserver-xorg \
        git

COPY . .
RUN pip install target/dist/alien_invasion-1.0/dist/Alien_Invasion-1.0-py3-none-any.whl && pip install pygame
CMD [ "python3", "alien_invasion.py" ]