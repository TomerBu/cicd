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
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update
RUN apt --fix-broken install
RUN apt-get install google-chrome-stable -y


# Install the Chrome WebDriver
# Install ChromeDriver.
RUN wget --no-check-certificate -N https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.58/linux64/chromedriver-linux64.zip -P ~/ && \
    unzip -o ~/chromedriver-linux64.zip -d ~/ && \
    rm ~/chromedriver-linux64.zip && \
    mv -f ~/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chown root:root /usr/local/bin/chromedriver && \
    chmod 0755 /usr/local/bin/chromedriver

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
