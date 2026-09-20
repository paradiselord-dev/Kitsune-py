# AfterImage: Extracción Incremental de Características

## 1. El Propósito
`AfterImage` actúa como el sistema nervioso central de Kitsune. Su misión es transformar el flujo caótico de paquetes de red (capas IP, TCP, UDP, etc.) en un **vector de características numéricas** que resuma el estado actual de las comunicaciones de la red.

## 2. ¿Cómo funciona sin saturar la RAM?
En lugar de almacenar una lista histórica de los últimos $N$ paquetes para calcular estadísticas, `AfterImage` implementa **Medias Móviles Exponenciales con decaimiento temporal (EMA)**. 
* Los eventos recientes tienen un peso mayor en el cálculo estadístico.
* Los eventos antiguos pierden influencia de forma exponencial y automática.
* Esto permite actualizar las métricas con una simple operación matemática instantánea cada vez que llega un paquete nuevo.

## 3. Las 5 Métricas Estadísticas Fundamentales
Para cada flujo de red (agrupado por tuplas de IP, puertos y protocolos) y a través de múltiples ventanas temporales (desde microsegundos hasta minutos), se extraen cinco dimensiones clave:

1. **Weight (Peso/Intensidad):** Cuántos paquetes han transitado en esa ventana ponderados por el tiempo.
2. **Mean (Media):** El tamaño promedio de los paquetes o la tasa media de llegada.
3. **Std (Desviación Estándar):** La variabilidad o fluctuación observada en el flujo.
4. **Radius (Radio):** La covarianza cruzada entre la velocidad de llegada y el tamaño del paquete.
5. **Magnitude (Magnitud):** La norma vectorial combinada de la intensidad de la conexión.

Como resultado, por cada paquete analizado, se emite un vector de alta dimensionalidad (típicamente 100 características) listo para ser evaluado por el detector de anomalías.