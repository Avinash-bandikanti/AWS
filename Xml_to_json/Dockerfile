# Use an official Python runtime as a parent image
FROM python:3.8-slim

RUN pip install xmltodict

# Set the working directory in the container
WORKDIR /app


# Copy the Python script to the container
COPY xml_to_json.py /app/
COPY xmlfile1.xml /app/
COPY xmlfile2.xml /app/



# Run the Python script when the container launches
ENTRYPOINT ["python","xml_to_json.py"]
