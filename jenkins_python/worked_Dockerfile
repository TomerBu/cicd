FROM jenkins/jenkins:lts

# switch to root user to install packages
USER root

# Install Python, pip, and virtualenv
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Firefox and Chromium
RUN apt-get install -y firefox-esr chromium

# Install Selenium using pip in the virtual environment
RUN pip3 install selenium

# Switch back to the jenkins user
# so that the Jenkins container runs as the jenkins user
USER jenkins
