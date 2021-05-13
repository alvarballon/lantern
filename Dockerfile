FROM python:3.8-slim-buster
COPY requirements.txt /src/requirements.txt
RUN pip3 install -r /src/requirements.txt
COPY shop_list_app.py /src
COPY shop_list /src/shop_list
EXPOSE 8050
CMD ["python", "/src/shop_list_app.py"]
