FROM continuumio/anaconda3:4.4.0
COPY . /user/banknoteapp/
EXPOSE 8000
WORKDIR /user/banknoteapp/
RUN pip install -r requirements.txt
RUN pip install -U scipy
CMD python app.py