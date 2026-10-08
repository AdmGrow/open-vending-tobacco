"""Test corto. Sin chequeo, sin metodo, bypass o reuso = no vende."""
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


def test_no_bypass():
    g = AgeGate()
    g.record(Check(passed=True, method="staff"))
    ok, reason = g.allow_vend()
    assert ok is False and reason == "no bypass"


def test_deny():
    g = AgeGate()
    ok, reason = vend_if_allowed(g, DenyVerifier())
    assert ok is False


def test_un_chequeo_no_se_reusa():
    g = AgeGate()
    g.record(Check(passed=True, method="documento"))
    ok, reason = g.allow_vend()
    assert ok is True and reason == "ok"
    g.consume()
    ok2, reason2 = g.allow_vend()
    assert ok2 is False and reason2 == "no age check"


if __name__ == "__main__":
    test_sin_chequeo()
    test_sin_metodo()
    test_no_bypass()
    test_deny()
    test_un_chequeo_no_se_reusa()
    print("ok: bloquea sin chequeo, sin metodo, bypass y reuso")
