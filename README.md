# Football Data Analyzer (CLI Tool)

## 1. Contexto y Narrativa

* **Stakeholder:** Analista deportivo especializado en apuestas de fútbol.  
* **Propuesta de Valor:** El analista necesita estadísticas confiables y rápidas sobre jugadores y equipos para tomar decisiones en tiempo real. Esta herramienta consulta una API pública de fútbol y muestra datos clave (goles, asistencias, partidos jugados) directamente en la terminal.

---

## 2. Configuración

El script usa variables de entorno para mayor seguridad.

| Variable | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `API_URL` | URL base de la API | `export API_URL="https://api-football-v1.p.rapidapi.com/v3"` |
| `API_KEY_PROYECTO` | Clave de acceso | `export API_KEY_PROYECTO="tu_clave"` |

> El archivo `.gitignore` protege credenciales y archivos sensibles.

---

## 3. Ejecución con Docker

### Opción A: Script automatizado
```bash
chmod +x build.sh
./build.sh
## Opción B: Manual
docker build -t football-analyzer .
docker run --name samplerunning -e API_URL=$API_URL -e API_KEY_PROYECTO=$API_KEY_PROYECTO football-analyzer

##4. Estructura del Proyecto
football-analyzer/
├── app.py              # Script principal de consulta API fútbol
├── build.sh            # Script de automatización (Docker build/run)
├── requirements.txt    # Dependencias
├── .gitignore          # Exclusiones
├── README.md           # Documentación
└── evidencias/
    ├── docker/
    │   ├── output.txt        # Logs de ejecución
    │   └── screenshot.png    # Captura de salida
    └── jenkins/
        ├── pipeline.png      # Pipeline en Jenkins
        └── console_output.txt # Logs de construcción

