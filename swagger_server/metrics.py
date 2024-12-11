from prometheus_client import Counter, Histogram


REQUEST_COUNT = Counter("app_requests_total", "Total number of requests to the application", ["method", "endpoint"])
REQUEST_LATENCY = Histogram("app_request_latency_seconds", "Latency of requests in seconds", ["method", "endpoint"])
REQUEST_STATUS_CODES = Counter(
    "app_requests_status_codes_total", 
    "Total number of requests by status code", 
    ["method", "endpoint", "status_code"]
)
ERROR_COUNT = Counter(
    "app_requests_errors_total", 
    "Total number of errors", 
    ["method", "endpoint"]
) 
