import os
from ultralytics import YOLO

# --- Definición de Rutas (Robusto) ---

# Ruta absoluta a este script (src/run_pipeline.py)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta a la raíz del proyecto (un nivel "arriba" de 'src')
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Ruta a la carpeta 'data'
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Ruta al vídeo de entrada
VIDEO_PATH = os.path.join(DATA_DIR, 'test_video.mp4') # El vídeo del Hito 2

# Ruta al config del tracker
# TRACKER_CONFIG = os.path.join(PROJECT_ROOT, 'bytetrack.yaml')
TRACKER_CONFIG = 'bytetrack.yaml' # Fuerzo a que use el config interno de la librería!
# --- Configuración del Modelo ---
MODEL_NAME = 'yolov8n.pt' # Modelo rápido para probar

def main():
    
    print("Iniciando pipeline de tracking...")
    print(f"  > Vídeo de entrada: {VIDEO_PATH}")
    print(f"  > Config de tracker: {TRACKER_CONFIG}")

    # 1. Validar que los archivos existen
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: No se encuentra el vídeo en {VIDEO_PATH}")
        return

    # 2. Cargar el modelo de detección (YOLOv8)
    print(f"Cargando modelo {MODEL_NAME}...")
    model = YOLO(MODEL_NAME)

    # 3. Ejecutar el TRACKING
    print("Ejecutando model.track()... Esto puede tardar.")
    results = model.track(
        source=VIDEO_PATH,
        tracker=TRACKER_CONFIG, # Aquí usamos nuestro config
        persist=True,           # Mantiene los IDs entre frames
        save=True,              # Resuelve Issue #19 (Guardar vídeo)
        save_txt=True,          # Resuelve Issue #18 (Guardar datos crudos)
        conf=0.3,               # Umbral de confianza
        iou=0.5                 # Umbral de IoU
    )
    
    print("\n¡Proceso de tracking completado!")
    print("Revisa la carpeta 'runs/detect/track' (o similar) para los resultados.")

if __name__ == "__main__":
    # Esto hace que el script se pueda ejecutar directamente
    main()