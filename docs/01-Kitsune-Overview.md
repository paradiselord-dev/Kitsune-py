# Kitsune: Arquitectura y Filosofía del Sistema

## 1. ¿Qué es Kitsune?
Kitsune es un **Sistema de Detección de Intrusiones en Red (NIDS)** en línea, de código abierto y **no supervisado**. A diferencia de los sistemas tradicionales que dependen de firmas estáticas conocidas o de costosos procesos de entrenamiento con tráfico previamente etiquetado (malicioso vs. benigno), Kitsune aprende a identificar patrones normales de tráfico de forma autónoma.

## 2. El Desafío del Monitoreo en Red en Tiempo Real
Los entornos de red modernos generan flujos masivos de paquetes a velocidades de gigabits por segundo. Los enfoques clásicos de Machine Learning chocan con dos grandes muros:
* **El cuello de botella de la memoria RAM:** Almacenar historiales de paquetes o ventanas deslizantes masivas satura rápidamente los recursos.
* **La latencia de procesamiento:** Analizar lotes de datos *offline* impide detectar un ataque en curso a tiempo de mitigarlo.

## 3. La Solución de Kitsune: Dos Etapas Modulares
Kitsune resuelve este dilema dividiendo el procesamiento en dos fases altamente eficientes y desacopladas:

1. **Extracción Incremental de Características (`AfterImage`):** Convierte cada paquete individual en un vector estadístico multidimensional en tiempo real, utilizando un consumo de memoria constante O(1).
2. **Detección de Anomalías por Ensemble de Autoencoders (`KitNET`):** Evalúa el flujo de vectores mediante una red neuronal ligera estructurada en capas jerárquicas, midiendo el error de reconstrucción (RMSE) para detectar anomalías instantáneas.