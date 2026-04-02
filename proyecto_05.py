import requests

ciudades = {
    "Bogotá":   {"lat": 4.7110, "lon": -74.0721},
    "Medellín": {"lat": 6.2442, "lon": -75.5812},
    "Cali":     {"lat": 3.4516, "lon": -76.5320},
    "Zarzal":   {"lat": 4.1532, "lon": -76.1611}
}

def consultar_clima(lat, lon, ciudad):
    url = "https://api.open-meteo.com/v1/forecast"
    
    parametros = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "timezone": "auto"
    }
    
    try:
        respuesta = requests.get(url, params=parametros)
        respuesta.raise_for_status()
        data = respuesta.json()
        
        clima = data["current"]
        temperatura = clima["temperature_2m"]
        humedad = clima["relative_humidity_2m"]
        viento = clima["wind_speed_10m"]
        
        if temperatura < 10:
            sensacion = "Frío"
        elif temperatura < 20:
            sensacion = "Fresco"
        elif temperatura < 30:
            sensacion = "Agradable"
        else:
            sensacion = "Caliente"
        
        print(f"\n===== CLIMA EN {ciudad.upper()} =====")
        print(f"Temperatura:  {temperatura}°C")
        print(f"Humedad:      {humedad}%")
        print(f"Viento:       {viento} km/h")
        print(f"Sensación:    {sensacion}\n")
    
    except requests.exceptions.RequestException as e:
        print("Error al consultar el clima:", e)
while True:
    print("=========== APP DEL CLIMA ==========")
    print("1. Bogotá")
    print("2. Medellín")
    print("3. Cali")
    print("4. Zarzal")
    print("5. Ingresar coordenadas manualmente")
    print("6. Salir")
    print("="*36)

    opcion = input("Selecciona una opción: ")
        
    if opcion in ["1", "2", "3", "4"]:
        ciudad = list(ciudades.keys())[int(opcion) - 1]
        coordenadas = ciudades[ciudad]
        consultar_clima(coordenadas["lat"], coordenadas["lon"], ciudad)
        
    elif opcion == "5":
        try:
            lat = float(input("Ingresa la latitud: "))
            lon = float(input("Ingresa la longitud: "))
            ciudad = input("Nombre de la ciudad: ")
            consultar_clima(lat, lon, ciudad)
        except ValueError:
            print("Coordenadas inválidas\n")
        
    elif opcion == "6":
        print("Saliendo de la app...")
        break
        
    else:
        print("Opción inválida\n")
    


