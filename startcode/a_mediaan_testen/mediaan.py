
def mediaan(getallen):
    """Geeft de mediaan van een lijst getallen."""
    if not getallen:
        raise ValueError("Lege lijst")

    getallen = sorted(getallen)
    midden = len(getallen) // 2
    return getallen[midden]

def test_mediaan():
    assert mediaan([1,3,2]) == 2
    assert mediaan([1,2,3,4]) == 2.5

mediaan(["1","2","3"])
test_mediaan()