from Kitsune import Kitsune
import numpy as np
import time

packet_path = "mirai.pcap"
limit = 120000
max_ae = 10
fm_grace = 2000
ad_grace = 10000

print("[*] Inicializando Kitsune...")
start_time = time.time()
K = Kitsune(
    file_path=packet_path,
    limit=limit,
    max_autoencoder_size=max_ae,
    FM_grace_period=fm_grace,
    AD_grace_period=ad_grace
)

rmse_results = []
count = 0

print(f"[*] Procesando hasta {limit} paquetes...")
try:
    while count < limit:
        rmse = K.proc_next_packet()
        
        # Criterio seguro compatible con arrays NumPy, floats o None
        if rmse is None:
            print("[+] Fin natural de los paquetes alcanzado.")
            break
        if hasattr(rmse, "__len__") and len(rmse) == 0:
            print("[+] Fin natural de los paquetes alcanzado.")
            break
            
        rmse_val = float(rmse) if not hasattr(rmse, "__len__") else float(rmse[0])
        rmse_results.append(rmse_val)
        count += 1
        
        if count % 10000 == 0:
            print(f"[+] Paquetes: {count} | Último RMSE: {rmse_val:.4f}")

except Exception as e:
    print(f"[!] Interrupción: {e}")

elapsed = time.time() - start_time
print(f"[+] Completado en {elapsed:.2f} s. Total procesados: {len(rmse_results)}")

np.save("rmse_results.npy", np.array(rmse_results))
print("[+] Resultados guardados en 'rmse_results.npy'")