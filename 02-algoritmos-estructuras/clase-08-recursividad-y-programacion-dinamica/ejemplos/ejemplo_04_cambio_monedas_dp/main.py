"""Problema del Cambio de Monedas."""
def cambio(monedas, monto):
    dp = [float('inf')] * (monto + 1)
    dp[0] = 0
    for m in monedas:
        for x in range(m, monto + 1):
            dp[x] = min(dp[x], dp[x - m] + 1)
    return dp[monto]
print('Monedas mínimas para $11:', cambio([1, 2, 5], 11))
