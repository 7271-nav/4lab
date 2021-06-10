FROM python:3
COPY main.py .
COPY sss.py .
ENTRYPOINT ["python", "main.py"] 
