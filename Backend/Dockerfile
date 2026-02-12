#base image
FROM python:3.10.13-slim

#workdir
WORKDIR /app/Backend

#copy
COPY Backend/requirements.txt /app/Backend/requirements.txt

#run
RUN python -m pip install --no-cache-dir -r requirements.txt

#copy
COPY Backend/ /app/Backend/
COPY model.pth /app/
COPY input.txt /app/

#port
EXPOSE 8000

#command
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
