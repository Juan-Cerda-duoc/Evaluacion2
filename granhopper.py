import urllib.parse
import time
import requests

KEY = "179d54a9-6f0e-4e63-a367-0b2b33cd383b"
GEO_URL = "https://graphhopper.com/api/1/geocode?"
ROUTE_URL = "https://graphhopper.com/api/1/route?"

T = {
    "es": {
        "exit_cmds": ("s", "salir", "q", "quit"),
        "vehicles": {
            "auto": "car",
            "bicicleta": "bike",
            "bici": "bike",
            "pie": "foot",
        },
        "v_title": "\nPerfiles de vehículo disponibles: auto, bicicleta, pie",
        "v_in": "Vehículo (o 's' / 'salir' para terminar): ",
        "loc1": "Origen (o 's' / 'salir'): ",
        "loc2": "Destino (o 's' / 'salir'): ",
        "route_hdr": "Ruta desde {n1} hasta {n2} en {v}",
        "dist_time": (
            "Distancia: {mi:.2f} mi / {km:.2f} km | Tiempo:"
            " {h:02d}:{m:02d}:{s:02d}"
        ),
        "narrative": (
            "Narrativa del viaje (secuencial por tiempo - cada 2 segundos):"
        ),
        "step": "Paso {i}: {txt} ({km:.2f} km / {mi:.2f} mi)",
        "err_loc": "Error: No se encontró alguna de las ubicaciones.",
        "err_route": "Error al calcular la ruta",
        "bye": "¡Programa finalizado!",
    },
    "en": {
        "exit_cmds": ("q", "quit"),
        "vehicles": {"car": "car", "bike": "bike", "foot": "foot"},
        "v_title": "\nAvailable vehicle profiles: car, bike, foot",
        "v_in": "Vehicle (or 'q' / 'quit' to exit): ",
        "loc1": "Origin (or 'q' / 'quit'): ",
        "loc2": "Destination (or 'q' / 'quit'): ",
        "route_hdr": "Route from {n1} to {n2} by {v}",
        "dist_time": (
            "Distance: {mi:.2f} mi / {km:.2f} km | Time:"
            " {h:02d}:{m:02d}:{s:02d}"
        ),
        "narrative": "Trip narrative (time-based sequential - every 2 seconds):",
        "step": "Step {i}: {txt} ({km:.2f} km / {mi:.2f} mi)",
        "err_loc": "Error: One of the locations was not found.",
        "err_route": "Error calculating route",
        "bye": "Program finished!",
    },
}


def geocode(loc, lang):
  url = GEO_URL + urllib.parse.urlencode(
      {"q": loc, "limit": "1", "key": KEY, "locale": lang}
  )
  res = requests.get(url).json()
  if res.get("hits"):
    h = res["hits"][0]
    name = ", ".join(
        filter(None, [h.get("name"), h.get("state"), h.get("country")])
    )
    return 200, h["point"]["lat"], h["point"]["lng"], name
  return 400, None, None, loc


opc = (
    input("Seleccione idioma / Select language (1: Español, 2: English) [1]: ")
    .strip()
)
lang = "en" if opc == "2" else "es"
txt = T[lang]

while True:
  print(txt["v_title"])
  v_in = input(txt["v_in"]).lower().strip()

  if v_in in txt["exit_cmds"]:
    break
  vehicle = txt["vehicles"].get(v_in, "car")

  loc1 = input(txt["loc1"]).strip()
  if loc1.lower() in txt["exit_cmds"]:
    break
  st1, lat1, lng1, name1 = geocode(loc1, lang)

  loc2 = input(txt["loc2"]).strip()
  if loc2.lower() in txt["exit_cmds"]:
    break
  st2, lat2, lng2, name2 = geocode(loc2, lang)

  if st1 == 200 and st2 == 200:
    p_url = (
        ROUTE_URL
        + urllib.parse.urlencode(
            {"key": KEY, "vehicle": vehicle, "locale": lang}
        )
        + f"&point={lat1}%2C{lng1}&point={lat2}%2C{lng2}"
    )
    res = requests.get(p_url)
    data = res.json()

    if res.status_code == 200 and "paths" in data:
      p = data["paths"][0]

      km, mi = p["distance"] / 1000, p["distance"] / 1000 / 1.61
      t = int(p["time"] / 1000)
      h, m, s = t // 3600, (t % 3600) // 60, t % 60

      print(
          f"\n{'='*50}\n" + txt["route_hdr"].format(n1=name1, n2=name2, v=vehicle)
      )
      print(
          txt["dist_time"].format(mi=mi, km=km, h=h, m=m, s=s) + f"\n{'='*50}"
      )
      print(txt["narrative"])

      steps = p["instructions"]
      total = len(steps)

      for i, step in enumerate(steps, 1):
        d_km = step["distance"] / 1000
        print(
            txt["step"].format(i=i, txt=step["text"], km=d_km, mi=d_km / 1.61)
        )

        if i < total:
          time.sleep(2)

      print("=" * 50)
    else:
      print("Error:", data.get("message", txt["err_route"]))
  else:
    print(txt["err_loc"])

print(txt["bye"])