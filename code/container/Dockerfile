FROM python:3.7-slim

RUN pip install numpy scipy scikit-learn==0.23.1

COPY inference.py /opt/ml/model/
WORKDIR /opt/ml/model/

CMD ["python", "-u", "inference.py"]
