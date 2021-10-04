FROM continuumio/anaconda3:4.4.0
COPY . /user/banknoteapp/
EXPOSE 8080
WORKDIR /user/banknoteapp/
RUN pip install -r requirements.txt
RUN pip install -U scipy
CMD python app.py