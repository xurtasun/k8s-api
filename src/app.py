import prometheus_client
from flask import Flask
import json, os

class Prometheus:
    def __init__(self, port = None, metric = None, description = None) -> None:
        self.metric = metric
        self.counter = prometheus_client.Counter(self.metric, description)
        prometheus_client.start_http_server(port)

    def increment(self):
        print(F"Incrementing {self.metric}...")
        self.counter.inc()


app = Flask(__name__)
prometheus = Prometheus(
    port = 8080,
    description = os.getenv('PROM_METRIC_DESCRIPTION','Counter of requests /data done.'),
    metric = os.getenv('PROM_METRIC_NAME','requests')
)


@app.route('/data', methods=['GET'])
def getData():
    with open('data.json') as data:
        prometheus.increment()
        return json.load(data)

@app.route('/ping', methods=['GET'])
def ping():
    return ('', 200)
