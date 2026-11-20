
from prometheus_client import start_http_server, Counter, Gauge
import time

# Define metrics
REQUEST_COUNT = Counter(
    'app_requests_total',
    'Total number of requests'
)

CPU_USAGE = Gauge(
    'app_cpu_usage',
    'Current CPU usage percentage'
)

def update_metrics():
    REQUEST_COUNT.inc()
    CPU_USAGE.set(25.0)

def main():
    start_http_server(8000)
    print("Metrics exporter running on port 8000")

    while True:
        update_metrics()
        time.sleep(5)

if __name__ == "__main__":
    main()
