import requests

def main():
    print("⚽ Buscador de jugadores - TheSportsDB")
    player_name = input("Ingrese el nombre del jugador: ")

    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={player_name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
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

    except requests.exceptions.Timeout:
        print("⏱ Error: la solicitud tardó demasiado.")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en la solicitud: {e}")

if __name__ == "__main__":
    main()

