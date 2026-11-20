
from app import REQUEST_COUNT, CPU_USAGE, update_metrics

def test_metrics_update():
    initial_count = REQUEST_COUNT._value.get()

    update_metrics()

    assert REQUEST_COUNT._value.get() == initial_count + 1

def test_cpu_usage():
    update_metrics()

    assert CPU_USAGE._value.get() == 25.0
