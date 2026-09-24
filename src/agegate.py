"""Age gate. Vend is blocked until a verifier returns pass.
Verifier is a plug-in (ID scanner, clerk PIN). No default pass.
"""
from dataclasses import dataclass

MIN_AGE_DEFAULT = 18

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
        if not self.last.passed:
            return False, "age check failed"
        if self.last.min_age < self.min_age:
            return False, "min age too low"
        return True, "ok"

    def consume(self):
        """One check per vend."""
        self.last = None
