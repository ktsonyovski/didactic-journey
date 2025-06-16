FROM ubuntu:latest

# Install Python 3.12 and pip system-wide
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Optional: Make python point to python3 for convenience
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl openjdk-17-jre python3 python3-pip && \
    apt-get clean

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Set environment variables for Poetry
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Copy project files
WORKDIR /app
COPY . .

# Install Python dependencies
RUN poetry install --no-interaction --no-ansi --no-root

# Install Jenkins
RUN curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null && \
    echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | tee /etc/apt/sources.list.d/jenkins.list > /dev/null && \
    apt-get update && \
    apt-get install -y fontconfig openjdk-17-jre jenkins

# Expose Jenkins port
EXPOSE 8080

# Start Jenkins
CMD ["bash", "-c", "service jenkins start && tail -f /var/log/jenkins/jenkins.log"]