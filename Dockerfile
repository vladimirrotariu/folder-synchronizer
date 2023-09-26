FROM python:3.11.5-bullseye

LABEL Name="Folder Synchronizer" Version=1.0.0

ARG srcDir=src
ARG main=folder_synchronizer
WORKDIR /app

COPY $srcDir/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY $srcDir/folder_synchronizer .

CMD ["python","folder_synchronizer.py"]
