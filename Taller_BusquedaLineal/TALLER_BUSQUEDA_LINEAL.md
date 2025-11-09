# TALLER PRÁCTICO: BÚSQUEDA LINEAL
## Sistema de Tienda de Electrónica

---

## 📋 INFORMACIÓN GENERAL

**Materia:** Algoritmos y Estructuras de Datos  
**Tema:** Búsqueda Lineal (Linear Search)  
**Duración:** 2 horas  
**Modalidad:** Práctica en laboratorio  

---

## 🎯 OBJETIVOS DE APRENDIZAJE

Al finalizar este taller, el estudiante será capaz de:

1. **Comprender** el concepto y funcionamiento del algoritmo de búsqueda lineal
2. **Implementar** búsqueda lineal en diferentes tipos de datos
3. **Analizar** la complejidad temporal del algoritmo O(n)
4. **Aplicar** búsqueda lineal en un contexto real (sistema de tienda)
5. **Diferenciar** entre búsqueda por valor exacto y búsqueda por criterios

---

## 📚 MARCO TEÓRICO

### ¿Qué es la Búsqueda Lineal?

La **búsqueda lineal** (también conocida como búsqueda secuencial) es un algoritmo simple que busca un elemento en una lista verificando cada elemento uno por uno hasta encontrar el elemento deseado o hasta que se hayan verificado todos los elementos.

### Características:
- **Complejidad Temporal:** O(n) - en el peor caso
- **Complejidad Espacial:** O(1) - espacio constante
- **No requiere datos ordenados**
- **Algoritmo estable**

### Pseudocódigo:
```
FUNCIÓN búsqueda_lineal(lista, elemento_buscado):
    PARA i = 0 HASTA longitud(lista) - 1:
        SI lista[i] == elemento_buscado:
            RETORNAR i
    RETORNAR -1  // No encontrado
```

---

## 🏪 CONTEXTO DEL PROBLEMA

### Sistema de Tienda de Electrónica "TechStore"

Necesitamos implementar un sistema de gestión para una tienda de electrónica que permita:

1. **Búsqueda de productos** por nombre, marca o categoría
2. **Búsqueda de empleados** por nombre, ID o departamento
3. **Búsqueda de disponibilidad** de productos por stock
4. **Gestión de inventario** básica

### Estructuras de Datos a Utilizar:

```python
# Estructura de un producto
producto = {
    'id': int,
    'nombre': str,
    'marca': str,
    'categoria': str,
    'precio': float,
    'stock': int,
    'disponible': bool
}

# Estructura de un empleado
empleado = {
    'id': int,
    'nombre': str,
    'apellido': str,
    'departamento': str,
    'salario': float,
    'activo': bool
}
```

---

## 🛠️ EJERCICIOS PRÁCTICOS

### EJERCICIO 1: Implementación Básica de Búsqueda Lineal

**Objetivo:** Implementar la función básica de búsqueda lineal

**Instrucciones:**
1. Crear una función `busqueda_lineal_simple(lista, elemento)` que busque un elemento en una lista de números
2. La función debe retornar el índice del elemento si lo encuentra, o -1 si no lo encuentra
3. Probar la función con diferentes casos

**Código base:**
```python
def busqueda_lineal_simple(lista, elemento):
    """
    Busca un elemento en una lista usando búsqueda lineal
    
    Args:
        lista: Lista de elementos
        elemento: Elemento a buscar
    
    Returns:
        int: Índice del elemento si se encuentra, -1 si no
    """
    # TODO: Implementar aquí
    
# Pruebas
numeros = [64, 34, 25, 12, 22, 11, 90]
print(busqueda_lineal_simple(numeros, 25))  # Debe retornar 2
print(busqueda_lineal_simple(numeros, 99))  # Debe retornar -1
```

### EJERCICIO 2: Búsqueda en Lista de Productos

**Objetivo:** Implementar búsqueda lineal en una lista de diccionarios

**Instrucciones:**
1. Crear una lista de productos de ejemplo
2. Implementar función para buscar producto por nombre
3. Implementar función para buscar producto por ID
4. Implementar función para buscar productos por categoría

**Datos de ejemplo:**
```python
productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True}
]
```

### EJERCICIO 3: Búsqueda de Empleados

**Objetivo:** Implementar búsqueda en lista de empleados

**Instrucciones:**
1. Crear lista de empleados
2. Implementar búsqueda por nombre completo
3. Implementar búsqueda por departamento
4. Implementar búsqueda de empleados activos

**Datos de ejemplo:**
```python
empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True}
]
```

### EJERCICIO 4: Búsqueda por Disponibilidad

**Objetivo:** Implementar búsquedas condicionales

**Instrucciones:**
1. Buscar productos disponibles (stock > 0)
2. Buscar productos por rango de precios
3. Buscar productos de una marca específica
4. Contar productos en una categoría

### EJERCICIO 5: Sistema Integrado

**Objetivo:** Crear un menú interactivo que integre todas las funciones

**Funcionalidades requeridas:**
1. Menú principal con opciones
2. Submenús para cada tipo de búsqueda
3. Validación de entrada del usuario
4. Manejo de errores básico
5. Opción de salir del programa

---

## 📝 ACTIVIDADES ADICIONALES

### Actividad 1: Análisis de Complejidad
- ¿Cuál es la complejidad temporal de cada función implementada?
- ¿En qué casos la búsqueda lineal es eficiente?
- ¿Cuándo sería mejor usar otro algoritmo de búsqueda?

### Actividad 2: Optimizaciones
- Implementar búsqueda que pare cuando encuentre el primer resultado
- Implementar búsqueda que retorne todos los resultados que coincidan
- Agregar contador de comparaciones realizadas

### Actividad 3: Casos Especiales
- ¿Qué pasa si la lista está vacía?
- ¿Cómo manejar búsquedas con mayúsculas/minúsculas?
- ¿Cómo buscar texto parcial en nombres?

---

## ✅ CRITERIOS DE EVALUACIÓN

### Funcionalidad (40%)
- [ ] Implementación correcta de búsqueda lineal básica
- [ ] Funciones de búsqueda en listas de diccionarios
- [ ] Manejo correcto de casos límite
- [ ] Sistema de menú funcional

### Calidad del Código (30%)
- [ ] Código bien comentado y documentado
- [ ] Nombres de variables descriptivos
- [ ] Estructura clara y organizada
- [ ] Manejo de errores

### Comprensión (20%)
- [ ] Explicación clara del algoritmo
- [ ] Identificación correcta de complejidad
- [ ] Respuestas a preguntas teóricas

### Creatividad (10%)
- [ ] Funcionalidades adicionales implementadas
- [ ] Mejoras en la interfaz de usuario
- [ ] Optimizaciones implementadas

---

## 📋 CHECKLIST DE ENTREGA

### Archivos a Entregar:
- [ ] `sistema_tienda.py` - Código principal del sistema
- [ ] `funciones_busqueda.py` - Funciones de búsqueda implementadas
- [ ] `datos_ejemplo.py` - Datos de prueba
- [ ] `README.md` - Documentación del proyecto
- [ ] `informe_taller.pdf` - Análisis y conclusiones

### Documentación Requerida:
- [ ] Comentarios en el código explicando cada función
- [ ] Ejemplos de uso de cada función
- [ ] Análisis de complejidad temporal
- [ ] Conclusiones sobre el algoritmo de búsqueda lineal

---

## 🚀 DESAFÍOS ADICIONALES

### Desafío 1: Búsqueda Avanzada
Implementar búsqueda que permita:
- Búsqueda por múltiples criterios simultáneamente
- Búsqueda con operadores lógicos (AND, OR)
- Búsqueda aproximada (tolerancia a errores de escritura)

### Desafío 2: Interfaz Gráfica
Crear una interfaz gráfica simple usando tkinter que permita:
- Visualizar resultados en una tabla
- Búsqueda en tiempo real mientras se escribe
- Filtros dinámicos

### Desafío 3: Persistencia de Datos
Implementar:
- Guardar y cargar datos desde archivos JSON
- Historial de búsquedas realizadas
- Estadísticas de uso del sistema

---

## 📚 RECURSOS ADICIONALES

### Enlaces de Referencia:
- [Algoritmos de Búsqueda - GeeksforGeeks](https://www.geeksforgeeks.org/searching-algorithms/)
- [Complejidad Computacional - Wikipedia](https://es.wikipedia.org/wiki/Complejidad_computacional)
- [Python Data Structures - Python.org](https://docs.python.org/3/tutorial/datastructures.html)

### Herramientas Recomendadas:
- **IDE:** Visual Studio Code, PyCharm
- **Control de Versiones:** Git
- **Testing:** pytest (opcional)
- **Documentación:** Markdown

---

## 💡 CONSEJOS PARA EL DESARROLLO

1. **Empieza simple:** Implementa primero la búsqueda básica
2. **Prueba frecuentemente:** Verifica cada función con datos de prueba
3. **Documenta tu código:** Comenta cada función y su propósito
4. **Maneja errores:** Considera casos donde la búsqueda puede fallar
5. **Optimiza después:** Primero haz que funcione, luego optimiza

---

**¡Buena suerte con tu taller de búsqueda lineal! 🚀**

*Recuerda: La práctica hace al maestro. No dudes en experimentar y probar diferentes enfoques.*
