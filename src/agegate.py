"""No vender si no controle la edad.

Esto es un ejercicio. No tengo lector todavia.
Un atajo de staff o admin no cuenta como chequeo.
"""
from dataclasses import dataclass

MIN_AGE_DEFAULT = 18
BLOCKED_METHODS = {"override", "staff", "bypass", "admin"}

@dataclass
class Check:
    passed: bool
    method: str
    min_age: int = MIN_AGE_DEFAULT

class AgeGate:
    def __init__(self, min_age: int = MIN_AGE_DEFAULT):
        self.min_age = min_age
        self.last = None

    def record(self, check: Check):
        self.last = check

    def allow_vend(self) -> tuple[bool, str]:
        if self.last is None:
            return False, "no age check"
        method = (self.last.method or "").strip().lower()
        if method in BLOCKED_METHODS:
            return False, "no bypass"
        if not self.last.passed:
            return False, "age check failed"
        if not method:
            return False, "no method"
        if self.last.min_age < self.min_age:
            return False, "min age too low"
        return True, "ok"

    def consume(self):
        # un chequeo por compra, si no se puede repetir
        self.last = None
