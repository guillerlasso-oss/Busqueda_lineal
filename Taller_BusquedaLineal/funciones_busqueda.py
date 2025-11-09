"""
funciones_busqueda.py
---------------------
Funciones de búsqueda lineal para el sistema de tienda "TechStore".

Cumple con:
- Implementación básica (Ejercicio 1).
- Búsquedas en listas de diccionarios (Ejercicios 2 y 3).
- Búsquedas condicionales (Ejercicio 4).
- Optimizaciones y contadores (Actividades adicionales).
- Soporte de coincidencia exacta y por criterios (may/min, parcial).
"""

from typing import Any, Dict, Iterable, List, Optional, Tuple, Callable

# -------------------------------
# Utilidades comunes
# -------------------------------

def normalizar_texto(s: str) -> str:
    """
    Convierte el texto a minúsculas y elimina espacios extremos.
    Maneja None de forma segura.
    """
    return (s or "").strip().lower()


# -------------------------------
# EJERCICIO 1: Búsqueda lineal simple
# -------------------------------

def busqueda_lineal_simple(lista: Iterable[Any], elemento: Any) -> int:
    """
    Busca un elemento en una lista usando búsqueda lineal.

    Args:
        lista (Iterable[Any]): Lista o iterable de elementos.
        elemento (Any): Elemento a buscar.

    Returns:
        int: Índice del elemento si se encuentra, -1 si no.
    """
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1


# Versión con contador de comparaciones (actividad adicional)
def busqueda_lineal_simple_contador(lista: Iterable[Any], elemento: Any) -> Tuple[int, int]:
    """
    Versión que además retorna el número de comparaciones realizadas.
    Returns: (indice, comparaciones)
    """
    comparaciones = 0
    for i, valor in enumerate(lista):
        comparaciones += 1
        if valor == elemento:
            return i, comparaciones
    return -1, comparaciones


# -------------------------------
# EJERCICIO 2: Búsqueda en lista de productos
# -------------------------------

Producto = Dict[str, Any]

def buscar_producto_por_nombre(productos: List[Producto], nombre: str, parcial: bool = False) -> List[Producto]:
    """
    Busca productos por nombre. Si parcial=True, realiza coincidencia parcial (subcadena).
    Devuelve lista de productos encontrados (puede estar vacía).
    """
    objetivo = normalizar_texto(nombre)
    resultados = []
    for p in productos:
        n = normalizar_texto(p.get('nombre'))
        if (n == objetivo) or (parcial and objetivo in n):
            resultados.append(p)
    return resultados


def buscar_producto_por_id(productos: List[Producto], id_producto: int) -> Optional[Producto]:
    """
    Devuelve el primer producto con id == id_producto, o None si no existe.
    """
    for p in productos:
        if p.get('id') == id_producto:
            return p
    return None


def buscar_productos_por_categoria(productos: List[Producto], categoria: str) -> List[Producto]:
    """
    Devuelve todos los productos de una categoría (case-insensitive).
    """
    cat = normalizar_texto(categoria)
    return [p for p in productos if normalizar_texto(p.get('categoria')) == cat]


# -------------------------------
# EJERCICIO 3: Búsqueda de empleados
# -------------------------------

Empleado = Dict[str, Any]

def buscar_empleado_por_nombre_completo(empleados: List[Empleado], nombre: str, apellido: str, parcial: bool = False) -> List[Empleado]:
    """
    Busca por nombre y apellido. Si parcial=True, permite subcadenas.
    Devuelve lista (0..n) empleados.
    """
    n_obj = normalizar_texto(nombre)
    a_obj = normalizar_texto(apellido)
    resultados = []
    for e in empleados:
        n = normalizar_texto(e.get('nombre'))
        a = normalizar_texto(e.get('apellido'))
        coincide = (n == n_obj and a == a_obj)
        if parcial:
            coincide = (n_obj in n) and (a_obj in a)
        if coincide:
            resultados.append(e)
    return resultados


def buscar_empleados_por_departamento(empleados: List[Empleado], departamento: str) -> List[Empleado]:
    dep = normalizar_texto(departamento)
    return [e for e in empleados if normalizar_texto(e.get('departamento')) == dep]


def buscar_empleados_activos(empleados: List[Empleado], activo: bool = True) -> List[Empleado]:
    return [e for e in empleados if bool(e.get('activo')) is activo]


# -------------------------------
# EJERCICIO 4: Búsqueda por disponibilidad y filtros
# -------------------------------

def filtrar_productos_disponibles(productos: List[Producto]) -> List[Producto]:
    """
    Productos con stock > 0 y disponible==True.
    """
    return [p for p in productos if p.get('stock', 0) > 0 and bool(p.get('disponible'))]


def filtrar_productos_por_rango_precio(productos: List[Producto], minimo: float = 0.0, maximo: float = float('inf')) -> List[Producto]:
    res = []
    for p in productos:
        precio = float(p.get('precio', 0.0))
        if minimo <= precio <= maximo:
            res.append(p)
    return res


def filtrar_productos_por_marca(productos: List[Producto], marca: str) -> List[Producto]:
    m = normalizar_texto(marca)
    return [p for p in productos if normalizar_texto(p.get('marca')) == m]


def contar_productos_por_categoria(productos: List[Producto], categoria: str) -> int:
    return len(buscar_productos_por_categoria(productos, categoria))


# -------------------------------
# DESAFÍO 1: Búsqueda avanzada (AND/OR, múltiples criterios, aproximada)
# -------------------------------

def _coincide_aproximado(texto: str, patron: str, tolerancia: int = 1) -> bool:
    """
    Coincidencia aproximada usando distancia de Levenshtein (implementación sencilla).
    Devuelve True si la distancia <= tolerancia.
    Nota: Implementación O(m*n), m=len(texto), n=len(patron); suficiente para listas pequeñas.
    """
    t = normalizar_texto(texto)
    p = normalizar_texto(patron)
    if p in t:
        return True
    # Programación dinámica para distancia de edición
    m, n = len(t), len(p)
    if n == 0:
        return True
    dp = list(range(n + 1))
    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            costo = 0 if t[i-1] == p[j-1] else 1
            dp[j] = min(
                dp[j] + 1,      # inserción
                dp[j-1] + 1,    # eliminación
                prev + costo    # sustitución
            )
            prev = temp
    return dp[n] <= tolerancia


def buscar_productos_avanzado(
    productos: List[Producto],
    criterios: Dict[str, Any],
    operador: str = "AND",
    aproximado: Optional[Dict[str, int]] = None
) -> List[Producto]:
    """
    Búsqueda por múltiples criterios.
    - criterios: dict con claves dentro de {'nombre','marca','categoria','min_precio','max_precio','disponible','min_stock'}
    - operador: 'AND' (todos los criterios) o 'OR' (alguno).
    - aproximado: dict opcional {'nombre': tolerancia, 'marca': tolerancia, ...} para coincidencia aproximada.
    """
    operador = operador.upper()
    def coincide(p: Producto) -> bool:
        checks: List[bool] = []

        # Nombre
        if 'nombre' in criterios:
            val = criterios['nombre']
            tol = (aproximado or {}).get('nombre', None)
            if tol is not None:
                checks.append(_coincide_aproximado(str(p.get('nombre','')), str(val), tol))
            else:
                checks.append(normalizar_texto(p.get('nombre')) == normalizar_texto(val))

        # Marca
        if 'marca' in criterios:
            val = criterios['marca']
            tol = (aproximado or {}).get('marca', None)
            if tol is not None:
                checks.append(_coincide_aproximado(str(p.get('marca','')), str(val), tol))
            else:
                checks.append(normalizar_texto(p.get('marca')) == normalizar_texto(val))

        # Categoría
        if 'categoria' in criterios:
            checks.append(normalizar_texto(p.get('categoria')) == normalizar_texto(criterios['categoria']))

        # Rango de precio
        precio = float(p.get('precio', 0.0))
        if 'min_precio' in criterios:
            checks.append(precio >= float(criterios['min_precio']))
        if 'max_precio' in criterios:
            checks.append(precio <= float(criterios['max_precio']))

        # Disponibilidad / stock
        if 'disponible' in criterios:
            checks.append(bool(p.get('disponible')) == bool(criterios['disponible']))
        if 'min_stock' in criterios:
            checks.append(int(p.get('stock', 0)) >= int(criterios['min_stock']))

        if not checks:
            return True  # sin criterios -> todo coincide
        return all(checks) if operador == 'AND' else any(checks)

    return [p for p in productos if coincide(p)]


# -------------------------------
# Funciones de ayuda para impresión
# -------------------------------

def formatear_producto(p: Producto) -> str:
    return (f"ID:{p.get('id')} | {p.get('nombre')} | Marca:{p.get('marca')} | "
            f"Cat:{p.get('categoria')} | Precio:{p.get('precio'):.2f} | "
            f"Stock:{p.get('stock')} | Disponible:{p.get('disponible')}")


def formatear_empleado(e: Empleado) -> str:
    return (f"ID:{e.get('id')} | {e.get('nombre')} {e.get('apellido')} | "
            f"Depto:{e.get('departamento')} | Salario:{e.get('salario'):.2f} | "
            f"Activo:{e.get('activo')}")


# -------------------------------
# Complejidades (para el informe)
# -------------------------------

COMPLEJIDADES = {
    'busqueda_lineal_simple': 'O(n) tiempo, O(1) espacio',
    'buscar_producto_por_nombre': 'O(n) tiempo (recorre todos los productos), O(1) espacio adicional',
    'buscar_producto_por_id': 'O(n) tiempo, O(1) espacio',
    'buscar_productos_por_categoria': 'O(n) tiempo, O(1) espacio',
    'buscar_empleado_por_nombre_completo': 'O(n) tiempo, O(1) espacio',
    'buscar_empleados_por_departamento': 'O(n) tiempo, O(1) espacio',
    'buscar_empleados_activos': 'O(n) tiempo, O(1) espacio',
    'filtrar_productos_disponibles': 'O(n) tiempo, O(1) espacio',
    'filtrar_productos_por_rango_precio': 'O(n) tiempo, O(1) espacio',
    'filtrar_productos_por_marca': 'O(n) tiempo, O(1) espacio',
    'contar_productos_por_categoria': 'O(n) tiempo (delegado), O(1) espacio',
    'buscar_productos_avanzado': 'O(n * k) tiempo aprox. (k=criterios), O(1) espacio',
}
