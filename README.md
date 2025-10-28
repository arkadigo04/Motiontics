# [MontionTics]

> TFG: Analiza partidos de fútbol para extraer estadísticas, detectar jugadas ofensivas/defensivas (YOLOv8, ByteTrack) y agrupar patrones tácticos (K-Means).

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Framework](https://img.shields.io/badge/Framework-FastAPI-green.svg)](https://fastapi.tiangolo.com/)
[![Deep Learning](https://img.shields.io/badge/Detección-YOLOv8-orange.svg)](https://docs.ultralytics.com/)

Este repositorio contiene el código fuente del Proyecto Fin de Grado de [Tu Nombre Aquí], que implementa un pipeline completo de Visión por Computador para el **análisis táctico y estadístico de partidos de fútbol**.

**Visita la Página Web del Proyecto (GitHub Pages) para ver los resultados:**
### [https://tu-usuario.github.io/tu-repo/](https://tu-usuario.github.io/tu-repo/)

---

## 🛠️ Stack Tecnológico

Este proyecto integra varias tecnologías punteras en el campo de la IA y el análisis deportivo:

* **Lenguaje:** Python 3.10+
* **Detección de Objetos:** **YOLOv8** (de Ultralytics). Es el "ojo" del sistema. Detecta jugadores, balón, árbitros y porterías en cada frame.
* **Tracking de Objetos:** **ByteTrack**. El algoritmo que sigue a cada jugador y al balón a lo largo del tiempo, asignando un ID único a cada uno (una trayectoria).
* **Clustering (Análisis):** **K-Means** (de Scikit-learn). Es el "cerebro táctico". Agrupa las trayectorias de los jugadores en patrones comunes para identificar **jugadas ofensivas (ej. contraataques), defensivas (ej. bloque bajo) o formaciones**.
* **API (Servidor):** **FastAPI**. El framework que "sirve" el análisis como un servicio web.
* **Procesamiento de Vídeo:** OpenCV

---

## 🧠 Arquitectura del Pipeline

El sistema transforma un vídeo de un partido en un JSON con estadísticas y patrones tácticos detectados.

*(Próximamente: Diagrama de arquitectura - FASE 6)*

1.  **Fase 1: Detección y Tracking (Posicionamiento)**
    * Un vídeo del partido es procesado frame a frame por OpenCV.
    * **YOLOv8** (entrenado para fútbol) detecta todos los jugadores y el balón.
    * **ByteTrack** recibe estas detecciones y asigna un `track_id` único a cada jugador, generando sus trayectorias completas.
    * Se genera un conjunto de datos crudos de posicionamiento (`{frame_id, track_id, bbox_jugador, bbox_balon}`).

2.  **Fase 2: Extracción de Features (Estadísticas)**
    * Los datos crudos de las trayectorias se transforman en **vectores de características** (un *resumen* numérico de la jugada o del jugador).
    * *Features (ej.):* Velocidad media del jugador, distancia recorrida, posesión del balón (proximidad al `track_id` del balón), mapa de calor (posición media), aceleraciones (sprints).

3.  **Fase 3: Clustering y Análisis (Táctica)**
    * **K-Means** agrupa estos vectores de características en *N* clusters.
    * Cada cluster representa un **patrón táctico o jugada común** (ej: "Cluster 0: Contraataque por banda derecha", "Cluster 1: Repliegue defensivo", "Cluster 2: Posesión en medio campo").
    * El resultado final es un JSON con las estadísticas y un resumen de las tácticas detectadas.

---

## 🗺️ Hoja de Ruta (Milestones)

Este proyecto se gestiona mediante Hitos (Milestones) y Tareas (Issues) en GitHub.

* ✅ **Hito 1: Fundación del Proyecto** (Due: 30 Oct, 2025)
* ◻️ **Hito 2: Detección Funcional** (Due: 24 Nov, 2025)
* ◻️ **Hito 3: Pipeline de Tracking (El Núcleo)** (Due: 20 Dic, 2025)
* ◻️ **Hito 4: Análisis y Clustering** (Due: 17 Ene, 2026)
* ◻️ **Hito 5: API (Productización)** (Due: 1 Feb, 2026)
* ◻️ **Hito 6: Despliegue y Presentación** (Due: 15 Feb, 2026)

---

## 🚀 Instalación y Uso

Sigue estos pasos para levantar el proyecto en tu máquina local.

#### 1. Clonar Repositorio
```bash
git clone [https://github.com/](https://github.com/)[tu-usuario]/[tu-repo].git
cd [tu-repo]
```

#### 2. Crear y Activar Entorno Virtual
(Recomendado: Python 3.10+)
```bash
python -m venv venv
source venv/bin/activate  # En Arch Linux / macOS / Linux
# .\venv\Scripts\activate  # En Windows
```

#### 3. Instalar Dependencias
Todas las dependencias están listadas en `requirements.txt`.
```bash
pip install -r requirements.txt
```
*(Esto instalará PyTorch/YOLOv8, OpenCV, Scikit-learn y FastAPI).*

---

### (Próximamente) Ejecución del Proyecto

#### 4. Ejecutar el Pipeline (Hito 3 y 4)
```bash
# (Instrucciones para ejecutar el análisis desde la terminal)
python src/pipeline.py --input data/partido_futbol.mp4 --output data/estadisticas_partido.json
```

#### 5. Levantar la API (Hito 5)
El servidor se lanza con `uvicorn`.
```bash
uvicorn src.main:app --reload
```
* Una vez activo, podrás acceder a la documentación interactiva de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
