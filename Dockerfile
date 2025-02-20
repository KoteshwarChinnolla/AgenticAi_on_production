# Use a base Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file into the container
COPY temp_venv.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt


COPY app.py app.py
COPY toolcallinglm.py toolcallinglm.py
COPY tools.py tools.py


EXPOSE 5000


CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]