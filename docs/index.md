---
title: "MotionTics - TFG Análisis Fútbol"
---

# MotionTics

### Un pipeline de Visión por Computador para el análisis táctico y estadístico de partidos de fútbol.

> **TFG:** Analiza vídeos de partidos de fútbol para extraer estadísticas, detectar jugadas ofensivas/defensivas (YOLOv8, ByteTrack) y agrupar patrones tácticos (K-Means).

---

## Objetivo del Proyecto

El objetivo de este proyecto es diseñar, implementar y validar un sistema capaz de procesar un vídeo de un partido de fútbol y **extraer automáticamente conocimiento táctico**.

El sistema identificará y seguirá a todos los jugadores y al balón (Detección + Tracking), para después **agrupar sus movimientos en "patrones tácticos"** (Clustering) sin supervisión humana. Esto permitirá generar resúmenes de jugadas (ofensivas, defensivas) y estadísticas de rendimiento (distancia, velocidad).

---

## Stack Tecnológico

* **Detección:** YOLOv8
* **Tracking:** ByteTrack
* **Clustering (Análisis):** K-Means (Scikit-learn)
* **API (Servidor):** FastAPI

---

## Hoja de Ruta (Milestones)

Este proyecto está actualmente en desarrollo.

* [✅] **Hito 1: Fundación del Proyecto** (30 Oct, 2025)
* [◻️] **Hito 2: Detección Funcional** (24 Nov, 2025)
* [◻️] **Hito 3: Pipeline de Tracking** (20 Dic, 2025)
* [◻️] **Hito 4: Análisis y Clustering** (17 Ene, 2026)
* [◻️] **Hito 5: API (Productización)** (1 Feb, 2026)
* [◻️] **Hito 6: Despliegue y Presentación** (15 Feb, 2026)

---

## Resultados (Próximamente)

* Demostración de Detección (YOLOv8).
* Demostración de Tracking (YOLOv8 + ByteTrack).
* Visualización de Clusters (K-Means).

---
> Proyecto Fin de Grado de [Arkaitz Diez Gonzalez] | [Universidad de Burgps] | 2025-2026
>
> [https://github.com/arkadigo04/Motiontics]
