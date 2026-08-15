# 📑 Cheatsheet: Fundamentos de Python

Resumen rápido de comandos y sintaxis esencial para consultar durante las clases.

---

## 🖨️ Mostrar en consola (`print`)
```python
print("Texto directo")
print(42)  # Números
print(f"Hola {nombre}")  # f-string (interpola variables)
```

---

## 📥 Solicitar datos (`input`)
```python
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))  # Convertir a entero
precio = float(input("Ingresa el precio: "))  # Convertir a decimal
```

---

## 🔢 Tipos de Datos
```python
texto = "Hola"       # str
entero = 10          # int
decimal = 3.14       # float
verdadero = True     # bool
falso = False        # bool
```

---

## 🔀 Condicionales (`if / elif / else`)
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres menor de edad")
```

---

## 🔁 Bucles / Loops

### Bucle `for` (Repetir N veces o recorrer elementos)
```python
for i in range(5):
    print(f"Número: {i}")
```

### Bucle `while` (Repetir mientras se cumpla una condición)
```python
contador = 0
while contador < 3:
    print("Repitiendo...")
    contador += 1
```

---

## 📦 Funciones (`def`)
```python
def saludar(nombre):
    return f"¡Hola {nombre}!"

mensaje = saludar("Ana")
print(mensaje)
```
