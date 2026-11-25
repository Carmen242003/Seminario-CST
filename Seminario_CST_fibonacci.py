def generar_fibonacci(n):
    """Genera los primeros n términos de la secuencia de Fibonacci."""
    if n <= 0:
        return []
    if n == 1:
        return [1]

    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    print(generar_fibonacci(9))
