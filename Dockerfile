FROM ubuntu:20.04
WORKDIR /var/www/namizun
ENV NAMIZUN_HOME=/var/www/namizun
RUN apt update && apt install python3-pip python3-venv redis git -y
COPY . /var/www/namizun
RUN pip install -r requirements.txt && pip install --no-build-isolation ./namizun_core ./namizun_menu
