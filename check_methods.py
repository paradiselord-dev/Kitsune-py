from Kitsune import Kitsune

# Inicializamos pasando los argumentos de forma posicional
Kitsune_instance = Kitsune("mirai.pcap", 10, 5000, 50000)

# Imprimimos todos los métodos públicos disponibles en el objeto
methods = [method for method in dir(Kitsune_instance) if not method.startswith('_')]
print("[+] Métodos disponibles en la clase Kitsune:", methods)