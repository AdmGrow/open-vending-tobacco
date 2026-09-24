"""Test de 10 lineas o menos. Sin chequeo = no vende."""
from src.agegate import AgeGate, Check
from src.verifier import DenyVerifier, vend_if_allowed

def test_sin_chequeo():
    g = AgeGate()
    ok, reason = g.allow_vend()
    assert ok is False and reason == "no age check"

def test_deny():
    g = AgeGate()
    ok, reason = vend_if_allowed(g, DenyVerifier())
    assert ok is False

if __name__ == "__main__":
    test_sin_chequeo()
    test_deny()
    print("ok: bloquea sin chequeo")
