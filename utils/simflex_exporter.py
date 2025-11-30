import json
import os

def convert_to_simflex(input_json):
    """
    Convert internal digital twin JSON schema into SimFlex-compatible scene JSON.
    """
    objects = []
    zones = input_json.get("layout", {}).get("zones", [])

    for zone in zones:
        zone_name = zone.get("name", "").lower().replace(" ", "_")

        # Machines
        for m in zone.get("machines", []):
            objects.append({
                "id": f"{zone_name}_{m.get('name','').lower().replace(' ', '_')}",
                "type": "machine",
                "model": m.get("model", None),
                "category": m.get("type", None),
                "position": m.get("location", {}),
                "rotation": m.get("rotation", 0),
                "parameters": {
                    "energy": m.get("energyConsumption", None),
                    "axes": m.get("kinematics", {}).get("axes", None),
                    "cycleTime": m.get("kinematics", {}).get("cycleTime", None)
                }
            })

        # Employees
        for e in zone.get("employees", []):
            objects.append({
                "id": f"{zone_name}_{e.get('name','').lower().replace(' ', '_')}",
                "type": "human",
                "role": e.get("position", None),
                "certification": e.get("certification", None),
                "position": e.get("location", {}),
                "rotation": 0
            })

        # Safety zones
        for s in zone.get("safetyZones", []):
            objects.append({
                "id": f"{zone_name}_safety_{s.get('type','').lower()}",
                "type": "safety_zone",
                "position": s.get("location", {}),
                "radius": s.get("radius", None)
            })

    return {"objects": objects}


def save_simflex_scene(scene_json, filename="simflex_scene.json", folder="./data"):
    """
    Save the SimFlex-compatible JSON to a file.
    """
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(scene_json, f, indent=4, ensure_ascii=False)

    print(f"🎨 SimFlex Scene saved at: {path}")
    return path
