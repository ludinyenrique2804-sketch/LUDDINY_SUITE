import random

@dataclass
class Failure(Exception):
    """"TIMEOUT DEL GATEWAY."""
    message: str
    code: Optional[int] = None

    def __str__(self):
        return f"[Error {self.code}] {self.message}" if self.code else self.message

class ConnectionFailure(Failure):
    """Error SERVICIO NO DISPONIBLE."""
    pass

class ExecutionFailure(Failure):
    """ERROR INTERNO DEL SISTEM."""
    pasimport random


def simulate_failure():
    return random.choice(FAILURES)
