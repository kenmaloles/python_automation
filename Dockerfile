FROM python:3.6-slim
COPY . /python_automation
WORKDIR /python_automation
RUN pip install --no-cache-dir -r requirements.txt
RUN ["pytest", "-v", "--junitxml=reports/result.xml"]
CMD tail -f /dev/null
