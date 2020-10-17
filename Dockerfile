FROM python:3.6-slim
COPY . /python_automation
WORKDIR /python_automation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# RUN python -u view.py
CMD tail -f /dev/null
RUN py.test -s jenkins_python/view.py