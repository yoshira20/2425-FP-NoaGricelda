# Crear una matriz 3D para almacenar datos de temperatura
# Primera dimensión: Ciudades (Puyo, Baños, Ambato)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semana (4 semanas)

temperaturas = [
    {"Ciudad": "Puyo", "Semanas": [
        [  # Semana 1
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 20},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 27},
            {"day": "Jueves", "temp": 17},
            {"day": "Viernes", "temp": 19},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 16},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 15}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 15},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 16},
            {"day": "Domingo", "temp": 14}
        ]
    ]},
    {"Ciudad": "Baños", "Semanas": [
        [  # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 8},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 16}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 12},
            {"day": "Jueves", "temp": 7},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 9},
            {"day": "Domingo", "temp": 15}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 7},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 6},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 14}
        ]
    ]},
    {"Ciudad": "Ambato", "Semanas": [
        [  # Semana 1
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 17},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 9}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 16},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 8}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 18},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 14},
            {"day": "Sábado", "temp": 9},
            {"day": "Domingo", "temp": 7}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 15},
            {"day": "Martes", "temp": 17},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 13},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 6}
        ]
    ]}
]

def calcular_temperatura_promedio(temperaturas):
    """
    Calcula el promedio de temperaturas de cada ciudad.
    """
    promedios = {}
    for ciudad in temperaturas:
        total_temp = sum(dia["temp"] for semana in ciudad["Semanas"] for dia in semana)
        total_dias = sum(len(semana) for semana in ciudad["Semanas"])
        promedios[ciudad["Ciudad"]] = round(total_temp / total_dias, 2)
    return promedios

# Llamar a la función y mostrar los resultados
resultados = calcular_temperatura_promedio(temperaturas)
print("\nPromedio de temperatura por ciudad:")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}ºC")







