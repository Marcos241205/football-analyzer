import os
import requests

def main():
    # Leer variables de entorno
    api_url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY_PROYECTO")

    if not api_url or not api_key:
        print("❌ Error: faltan variables de entorno API_URL o API_KEY_PROYECTO")
        return

    # Endpoint de ejemplo: información de un equipo
    endpoint = f"{api_url}/teams?id=33"  # ID 33 = Manchester United (ejemplo)
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    try:
        response = requests.get(endpoint, headers=headers, timeout=10)
        response.raise_for_status()  # lanza excepción si el status != 200
        data = response.json()

        # Mostrar datos clave
        team = data.get("response", [{}])[0].get("team", {})
        print("✅ Conexión exitosa a la API")
        print(f"Equipo: {team.get('name')}")
        print(f"País: {team.get('country')}")
        print(f"Fundado en: {team.get('founded')}")

    except requests.exceptions.Timeout:
        print("⏱ Error: la solicitud a la API tardó demasiado.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la solicitud: {e}")

if __name__ == "__main__":
    main()
