# start by pulling the python image
FROM python:3.8-alpine

# copy the requirements file into the image
COPY ./requirements.txt /aspencapitalchallenge/requirements.txt

# switch working directory
WORKDIR /aspencapitalchallenge

# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /aspencapitalchallenge

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]