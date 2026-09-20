# KitNET: Detección de Anomalías mediante Autoencoders

## 1. ¿Qué es KitNET?
`KitNET` es un detector de anomalías basado en un **Ensamblaje de Autoencoders** (redes neuronales sin supervisión entrenadas para replicar su entrada en la salida). Está diseñado específicamente para operar de forma incremental y ligera en dispositivos con recursos limitados.

## 2. Arquitectura Jerárquica en Capas
Para evitar que un único autoencoder gigante sufra de sobreajuste o sea computacionalmente inviable, KitNET organiza sus redes en una estructura de tres niveles:

* **Capa 1 (Mapping Layer / Capa de Mapeo):** Cada autoencoder de esta capa recibe un subconjunto específico de las características extraídas por `AfterImage` (agrupando métricas correlacionadas). Aprenden a reconstruir sus entradas locales y emiten un error de reconstrucción individual.
* **Capa 2 (Reduction Layer / Capa de Reducción):** Un segundo nivel de autoencoders que recibe y comprime los errores de reconstrucción de la Capa 1, encontrando correlaciones de alto nivel entre los diferentes grupos de características.
* **Capa de Salida (Output Layer):** Un autoencoder final que consolida la salida de la Capa 2 para generar una métrica global unificada.

## 3. El Indicador de Anomalía: RMSE
El rendimiento de todo el ensamblaje se mide mediante el **Error Cuadrático Medio de Reconstrucción (Root Mean Square Error - RMSE)**:
* **Tráfico Normal:** Los autoencoders, al haber aprendido los patrones habituales durante el periodo de gracia (*grace period*), reconstruyen las entradas con un error mínimo (RMSE cercano a 0).
* **Tráfico Malicioso / Anomalía:** Cuando ocurre un evento anómalo (como un escaneo de puertos de Mirai, una inundación SYN o exfiltración), las correlaciones estadísticas cambian drásticamente. Los autoencoders fallan al intentar replicar ese patrón desconocido, provocando un **pico abrupto y masivo en el RMSE**, lo que dispara la alerta de intrusión de forma inmediata.