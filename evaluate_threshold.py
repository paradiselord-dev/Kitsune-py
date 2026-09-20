import numpy as np
import matplotlib.pyplot as plt

# Cargar datos
rmse = np.load("rmse_results.npy")

# Segmento benigno conocido (justo tras el entrenamiento: 12k a 30k)
baseline_start = 12000
baseline_end = 30000
baseline = rmse[baseline_start:baseline_end]

mu = np.mean(baseline)
sigma = np.std(baseline)
beta = 3  # Regla empírica de 3 sigmas (99.7% confianza bajo normalidad)
threshold = mu + beta * sigma

# Evaluación sobre todo el tramo activo (paquete 12000 en adelante)
active_rmse = rmse[baseline_start:]
anomalies = active_rmse > threshold
total_active = len(active_rmse)
total_anomalies = np.sum(anomalies)
ratio_anom = (total_anomalies / total_active) * 100

print(f"[*] Estadísticas de línea base (paquetes {baseline_start}-{baseline_end}):")
print(f"    Media (mu): {mu:.4f}")
print(f"    Desv. Estándar (sigma): {sigma:.4f}")
print(f"    Umbral calculado (mu + {beta}*sigma): {threshold:.4f}\n")
print(f"[*] Resumen de detección:")
print(f"    Paquetes evaluados: {total_active}")
print(f"    Alertas / Paquetes anómalos: {total_anomalies} ({ratio_anom:.2f}%)")

# Graficar con el umbral superpuesto
plt.figure(figsize=(12, 5))
plt.plot(rmse, color="#1f77b4", linewidth=0.8, label="RMSE (KitNET)")
plt.axvline(x=12000, color="red", linestyle="--", linewidth=1, label="Inicio execute-mode")
plt.axhline(y=threshold, color="orange", linestyle="-.", linewidth=1.2, label=f"Umbral ({threshold:.3f})")

plt.yscale("log")
plt.title("KitNET - Detección de Anomalías con Umbral Estadístico", fontsize=13)
plt.xlabel("Índice de Paquete", fontsize=11)
plt.ylabel("RMSE (log scale)", fontsize=11)
plt.grid(True, which="both", linestyle=":", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig("rmse_threshold_log.png", dpi=300)
print("[+] Gráfico guardado como 'rmse_threshold_log.png'")
plt.show()