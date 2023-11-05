# Use the official Ubuntu as the base image
FROM ubuntu:latest

# Update package lists and install necessary packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev && \
    pip3 install numpy pandas seaborn matplotlib scikit-learn scipy

# Create a directory inside the container at /home/doc-bd-a3
RUN mkdir -p /home/doc-bd-a3

# Copy the dataset file from your local machine to the container
COPY 1.csv /home/doc-bd-a3/1.csv

# Set the working directory to /home/doc-bd-a3
WORKDIR /home/doc-bd-a3

# Start a bash shell when the container starts
CMD ["/bin/bash"]

