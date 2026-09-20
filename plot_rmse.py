import numpy as np
import matplotlib.pyplot as plt

rmse_data = np.load("rmse_results.npy")
clean_rmse = np.where(rmse_data < 0, 0, rmse_data)

plt.figure(figsize=(12, 5))
plt.plot(clean_rmse, color="#1f77b4", linewidth=0.8, label="RMSE (KitNET)")
plt.axvline(x=12000, color="red", linestyle="--", linewidth=1, label="Inicio execute-mode (12k)")

# Escala semilogarítmica para ver detalles en valores cercanos a cero
plt.yscale("log")

plt.title("KitNET Anomaly Detection - Mirai Dataset (Escala Logarítmica)", fontsize=13)
plt.xlabel("Índice de Paquete", fontsize=11)
plt.ylabel("RMSE (log scale)", fontsize=11)
plt.grid(True, which="both", linestyle=":", alpha=0.6)
plt.legend(loc="upper right")
plt.tight_layout()

plt.savefig("mirai_rmse_log_plot.png", dpi=300)
print("[+] Gráfico guardado como 'mirai_rmse_log_plot.png'")
plt.show()