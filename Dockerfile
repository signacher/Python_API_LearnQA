FROM python
WORKDIR /python-api-learn/
COPY requirements.txt .
RUN pip3 install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /python-api-learn/tests/