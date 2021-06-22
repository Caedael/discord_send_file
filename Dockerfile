FROM python:slim
ADD script.py /
ADD embeds.py /
RUN pip install discord_webhook requests 
#CMD ["python", "/script.py"]
