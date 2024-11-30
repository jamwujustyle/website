FROM python

WORKDIR /reminder
COPY . /reminder/
RUN pip install  --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]