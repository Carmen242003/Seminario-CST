import matplotlib.pyplot as plt
import numpy as np


def generar_fibonacci(n):
    """Genera los primeros n términos de la secuencia de Fibonacci."""
    if n <= 0:
        return []
    if n == 1:
        return [1]

    secuencia = [1, 1]
    while len(secuencia) < n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia


def dibujar_crecimiento(secuencia, guardar=False):
    """Dibuja la evolución de los términos de la secuencia de Fibonacci."""
    indices = np.arange(1, len(secuencia) + 1)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(
        indices,
        secuencia,
        marker="o",
        color="#2b5c8f",
        linewidth=2,
        markersize=7,
        label="F(n)",
    )
    ax.bar(indices, secuencia, color="#7fa8d4", alpha=0.35)
    ax.set_title("Crecimiento de la secuencia de Fibonacci")
    ax.set_xlabel("Término (n)")
    ax.set_ylabel("Valor F(n)")
    ax.set_xticks(indices)
    ax.grid(True, linestyle="--", alpha=0.6)

    if len(secuencia) <= 12:
        for i, val in enumerate(secuencia):
            ax.annotate(
                str(val),
                (indices[i], val),
                textcoords="offset points",
                xytext=(0, 8),
                ha="center",
                fontsize=9,
            )

    plt.tight_layout()
    if guardar:
        plt.savefig("crecimiento_fibonacci.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    seq = generar_fibonacci(9)
    print(seq)
    dibujar_crecimiento(seq)
