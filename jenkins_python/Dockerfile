FROM jenkins/jenkins:lts

# Switch to root user to install packages
USER root

# Install necessary utilities
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv wget gnupg2 software-properties-common

# Create a virtual environment and activate it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Firefox, Chromium
RUN apt-get install -y firefox-esr chromium

# Add Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm ./google-chrome-stable_current_amd64.deb

# Add Google Chrome to the PATH
ENV PATH="/usr/bin/google-chrome:$PATH"

# Add Microsoft's repository for Edge
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" && \
    apt-get update

# Install Microsoft Edge
RUN apt-get install -y microsoft-edge-stable

# Install Selenium using pip in the virtual environment
RUN pip3 install selenium

# Switch back to the jenkins user
# so that the Jenkins container runs as the jenkins user
USER jenkins
