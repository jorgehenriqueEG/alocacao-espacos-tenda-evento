def alocar_expositores(expositores, limite_area=100):
    ordenados = sorted(expositores, key=lambda x: x["valor"], reverse=True)
    aceitos = []
    total_area = 0

    for exp in ordenados:
        if total_area + exp["area"] <= limite_area:
            aceitos.append(exp["nome"])
            total_area += exp["area"]
        else:
            break

    return aceitos, total_area

data = [
    {"nome": "TechCorp", "area": 50, "valor": 5000},
    {"nome": "Foodie", "area": 30, "valor": 3000},
    {"nome": "GamerZone", "area": 40, "valor": 8000},
    {"nome": "StartupXYZ", "area": 20, "valor": 1000}
]

result, area_usada = alocar_expositores(data)

print("Expositores Alocados:")
for nome in result:
    print(f"- {nome}")
print(f"Área Total Utilizada: {area_usada}m2")