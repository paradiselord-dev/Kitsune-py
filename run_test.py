from Kitsune import Kitsune
import time

# Inicialización posicional basada en la estructura descubierta
packet_path = "mirai.pcap"
maxAE = 10          
FMgrace = 5000      
ADgrace = 50000     

print("[*] Inicializando el motor Kitsune...")
start_time = time.time()
Kitsune_instance = Kitsune(packet_path, maxAE, FMgrace, ADgrace)

print("[*] Ejecutando el pipeline iterativo de procesamiento (RMSE)...")
rmse_results = []

# Iteramos paquete por paquete utilizando proc_next_packet
# (Este bucle procesará todo el archivo .tsv generado previamente)
try:
    while True:
        # proc_next_packet procesa el siguiente vector y devuelve el error RMSE correspondiente
        rmse = Kitsune_instance.proc_next_packet()
        if rmse is None:
            break
        rmse_results.append(rmse)
except Exception as e:
    print(f"[!] Fin del flujo o aviso: {e}")

elapsed = time.time() - start_time
print(f"[+] ¡Procesamiento completado en {elapsed:.2f} segundos!")
print(f"[+] Total de puntos de RMSE recopilados: {len(rmse_results)}")
print(f"[+] Primeros valores de RMSE (muestra): {rmse_results[:5]}")