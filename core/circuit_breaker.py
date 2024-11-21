from pybreaker import CircuitBreaker, CircuitBreakerError

CIRCUIT_BREAKER_ERROR = CircuitBreakerError

failure_threshold = 3
success_threshold = 5
reset_timeout = 10

breaker = CircuitBreaker(
    fail_max=failure_threshold,
    reset_timeout=reset_timeout
)
