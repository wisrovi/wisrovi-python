"""Ejercicio: Cálculo de similitud de coseno para búsqueda semántica RAG."""
import math

def similitud_coseno(vec_a: list[float], vec_b: list[float]) -> float:
    if len(vec_a) != len(vec_b) or not vec_a:
        return 0.0
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)

if __name__ == "__main__":
    v1 = [1.0, 2.0, 3.0]
    v2 = [1.0, 2.0, 3.0]
    print("Similitud:", similitud_coseno(v1, v2))
