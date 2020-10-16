FROM python:3.6-slim
COPY . /python_automation
WORKDIR /python_automation
RUN pip install --no-cache-dir -r requirements.txt
# Install Chrome for Selenium
RUN curl https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o /chrome.deb
RUN dpkg -i /chrome.deb || apt-get install -yf
RUN rm /chrome.deb

# Install chromedriver for Selenium
RUN curl https://chromedriver.storage.googleapis.com/2.31/chromedriver_linux64.zip -o /usr/local/bin/chromedriver
RUN chmod +x /usr/local/bin/chromedriver

RUN py.test -s jenkins_python/view.py
# RUN python -u view.py
CMD tail -f /dev/null
