def test_c2_clase_07():
    grafo = {"A": ["B"], "B": ["C"], "C": []}
    assert "B" in grafo["A"]
