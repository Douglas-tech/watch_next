FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD python watch_next.py