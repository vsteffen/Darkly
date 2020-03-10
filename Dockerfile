FROM kalilinux/kali-rolling

RUN set -x \
    && apt-get -yqq update \
    && apt-get -yqq dist-upgrade \
    && apt-get clean

RUN apt-get install -y git vim curl hydra dirb python2 python-pip \
    && pip install Scrapy requests

RUN mkdir -p /root/dictionary \
  && curl -k https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-500.txt -o /root/dictionary/10-million-password-list-top-500.txt

RUN git clone https://github.com/vsteffen/darkly /root/darkly

WORKDIR /root/darkly

CMD ["bash"]
