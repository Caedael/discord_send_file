FROM python:slim
ADD script.py /
RUN pip install discord_webhook
CMD ["python", "./script.py"]
