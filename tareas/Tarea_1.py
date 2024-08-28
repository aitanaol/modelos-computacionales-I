# Tarea 1

## Crear lista
colores = ["rojo", "naranja", "amarillo", "verde", "azul", "morado", "rosa"]
print(colores)

### Ejercicios de práctica

colores.append("negro")
print(colores)

frutas = ["fresa", "mandarina", "platano"]
colores.extend(frutas)
print(colores)

colores.insert(4, "blanco")
print(colores)
colores.insert(0, "blanco")
print(colores)
colores.insert(len(colores), "blanco")
print(colores)
print(colores.count("blanco"))

colores.remove("blanco")
print(colores)

colores.pop(4)
print(colores)
colores.pop()
print(colores)

colores.index("rosa")
print(colores.index("rosa"))

colores.sort()
print(colores)

colores.reverse()
print(colores)

colores.copy()
print(colores)

colores.clear()
print(colores)