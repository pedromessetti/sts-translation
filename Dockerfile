FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Install necessary packages
RUN apt-get update && \
    apt-get install -y pulseaudio && \
		apt-get install -y gcc portaudio19-dev python3-pyaudio && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the PulseAudio server environment variable
ENV PULSE_SERVER=unix:${XDG_RUNTIME_DIR}/pulse/native

# Copy the current directory contents into the container at /app
COPY sps.py .

# Install any needed packages
RUN pip install --upgrade googletrans SpeechRecognition gtts pygame pyaudio

EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "sps.py"]

# Run the following command to build the Docker image:
# docker build -t sps .

# Run the following command to run the Docker image:
# docker run -p 8080:8080 sps
