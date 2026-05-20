import requests

def main():
    print("⚽ Buscador de jugadores - TheSportsDB")
    player_name = input("Ingrese el nombre del jugador: ")

    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={player_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
import requests
import sys

def main():
    print("⚽ Buscador de jugadores - TheSportsDB")
    
    # Sistema automático para Jenkins: si pasas un argumento lo usa, si no, usa uno por defecto
    if len(sys.argv) > 1:
        player_name = sys.argv[1]
    else:
        player_name = "Alexis Sanchez"
        
    print(f"Buscando información de: {player_name}")

    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={player_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Esto activa los errores HTTP (como 404 o 500)
        data = response.json()

        players = data.get("player")
        if not players:
            print("❌ No se encontraron jugadores con ese nombre.")
            return

        player = players[0]  # muestra el primero encontrado
        print("\n✅ Datos del jugador:")
        print(f"Nombre: {player.get('strPlayer')}")
        print(f"Equipo actual: {player.get('strTeam')}")
        print(f"Nacionalidad: {player.get('strNationality')}")
        print(f"Posición: {player.get('strPosition')}")
        print(f"Fecha de nacimiento: {player.get('dateBorn')}")
        print(f"Descripción: {player.get('strDescriptionEN')[:200]}...")  # resumen

    # Cumpliendo con la rúbrica: Manejo de al menos 4 tipos de errores
    except requests.exceptions.Timeout:
        print("⏱️ Error: la solicitud tardó demasiado.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Error HTTP encontrado: {e}")
    except requests.exceptions.ConnectionError:
        print("❌ Error de conexión: No se pudo conectar al servidor de la API.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error general en la solicitud: {e}")

if __name__ == "__main__":
    main()
