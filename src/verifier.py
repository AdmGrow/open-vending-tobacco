"""Por ahora el verificador dice que no.
Cuando tenga un lector lo cambio.
"""
from abc import ABC, abstractmethod
from .agegate import Check, AgeGate

class Verifier(ABC):
    @abstractmethod
    def check(self) -> Check:
        ...

class DenyVerifier(Verifier):
    def check(self) -> Check:
        return Check(passed=False, method="deny-default")

def vend_if_allowed(gate: AgeGate, verifier: Verifier) -> tuple[bool, str]:
    gate.record(verifier.check())
    ok, reason = gate.allow_vend()
    if ok:
        gate.consume()
    return ok, reason
