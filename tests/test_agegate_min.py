"""Test corto. Sin chequeo o sin metodo = no vende."""
from src.agegate import AgeGate, Check
from src.verifier import DenyVerifier, vend_if_allowed

def test_sin_chequeo():
    g = AgeGate()
    ok, reason = g.allow_vend()
    assert ok is False and reason == "no age check"

def test_sin_metodo():
    g = AgeGate()
    g.record(Check(passed=True, method="  "))
    ok, reason = g.allow_vend()
    assert ok is False and reason == "no method"

def test_deny():
    g = AgeGate()
    ok, reason = vend_if_allowed(g, DenyVerifier())
    assert ok is False

if __name__ == "__main__":
    test_sin_chequeo()
    test_sin_metodo()
    test_deny()
    print("ok: bloquea sin chequeo y sin metodo")
