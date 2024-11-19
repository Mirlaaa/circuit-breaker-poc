from pybreaker import CircuitBreaker

failure_threshold = 3
success_threshold = 5
reset_timeout = 10

breaker = CircuitBreaker(
    fail_max=failure_threshold,
    reset_timeout=reset_timeout
)
