"================ Sistema de Tienda ================"

from typing import List, Dict
from funciones_busqueda import (busqueda_lineal_simple, busqueda_lineal_simple_contador, buscar_producto_por_nombre,
                                buscar_producto_por_id, buscar_productos_por_categoria, buscar_empleado_por_nombre_completo, buscar_empleados_por_departamento,
                                buscar_empleados_activos, filtrar_productos_disponibles, filtrar_productos_por_rango_precio, filtrar_productos_por_marca, contar_productos_por_categoria,
                                buscar_productos_avanzado, formatear_producto, formatear_empleado 
                                )

from datos_ejemplo import productos, empleados

def imprimir_lista_productos(lista: List[Dict]):
    if not lista:
        print("(sin resultados)")
        return
    for p in lista:
        print(" - ", formatear_producto(p))

def imprimir_lista_empleados(lista: List[Dict]):
    if not lista:
        print("(sin resultados)")
        return
    for e in lista:
        print(" - ", formatear_empleado(e))

def menu_principal():
    while True:
        print("""
================= TechStore =================
1) Búsqueda lineal simple (lista de números)
2) Búsqueda en lista de productos
3) Búsqueda de empleados
4) Búsquedas por disponibilidad y filtros
5) Búsqueda avanzada (AND/OR/Aproximada)
0) Salir
=============================================
""")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            numeros = [64, 34, 25, 12, 22, 11, 90]
            print("Lista:", numeros)
            try:
                x = int(input("Número a buscar: ").strip())
            except ValueError:
                print("Entrada inválida.")
                continue
            indice, comps = busqueda_lineal_simple_contador(numeros, x)
            print(f"Resultado: índice={indice}, comparaciones={comps}")

        elif opcion == '23':
            submenu_productos()

        elif opcion == '3':
            submenu_empleados()

        elif opcion == '4':
            submenu_disponibilidad()

        elif opcion == '5':
            submenu_avanzado()

        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def submenu_productos():
    while True:
        print("""
-- Productos --
1) Buscar por nombre (exacto)
2) Buscar por nombre (parcial)
3) Buscar por ID
4) Buscar por categoría
0) Volver
""")
        opcion = input("Seleccione: ").strip()
        if opcion == '1':
            nombre = input("Nombre exacto: ")
            res = buscar_producto_por_nombre(productos, nombre, parcial=False)
            imprimir_lista_productos(res)
        elif opcion == '2':
            nombre = input("Cadena a buscar en nombre: ")
            res = buscar_producto_por_nombre(productos, nombre, parcial=True)
            imprimir_lista_productos(res)
        elif opcion == '3':
            try:
                pid = int(input("ID de producto: ").strip())
            except ValueError:
                print("ID inválido.")
                continue
            p = buscar_producto_por_id(productos, pid)
            if p:
                imprimir_lista_productos([p])
            else:
                print("No encontrado.")
        elif opcion == '4':
            cat = input("Categoría: ")
            res = buscar_productos_por_categoria(productos, cat)
            imprimir_lista_productos(res)
        elif opcion == '0':
            break
        else:
            print("Opción inválida.")

def submenu_empleados():
    while True:
        print("""
-- Empleados --
1) Buscar por nombre y apellido (exacto)
2) Buscar por nombre y apellido (parcial)
3) Buscar por departamento
4) Listar activos
0) Volver
""")
        opcion = input("Seleccione: ").strip()
        if opcion == '1':
            n = input("Nombre: ")
            a = input("Apellido: ")
            res = buscar_empleado_por_nombre_completo(empleados, n, a, parcial=False)
            imprimir_lista_empleados(res)
        elif opcion == '2':
            n = input("Nombre (subcadena): ")
            a = input("Apellido (subcadena): ")
            res = buscar_empleado_por_nombre_completo(empleados, n, a, parcial=True)
            imprimir_lista_empleados(res)
        elif opcion == '3':
            d = input("Departamento: ")
            res = buscar_empleados_por_departamento(empleados, d)
            imprimir_lista_empleados(res)
        elif opcion == '4':
            res = buscar_empleados_activos(empleados, True)
            imprimir_lista_empleados(res)
        elif opcion == '0':
            break
        else:
            print("Opción inválida.")

def submenu_disponibilidad():
    while True:
        print("""
-- Disponibilidad y Filtros --
1) Productos disponibles (stock>0 y disponibles)
2) Productos por rango de precio
3) Productos por marca
4) Contar productos por categoría
0) Volver
""")
        opcion = input("Seleccione: ").strip()
        if opcion == '1':
            res = filtrar_productos_disponibles(productos)
            imprimir_lista_productos(res)
        elif opcion == '2':
            try:
                minimo = float(input("Precio mínimo: ").strip() or 0)
                maximo = float(input("Precio máximo (ENTER para infinito): ").strip() or float('inf'))
            except ValueError:
                print("Valores inválidos.")
                continue
            res = filtrar_productos_por_rango_precio(productos, minimo, maximo)
            imprimir_lista_productos(res)
        elif opcion == '3':
            marca = input("Marca: ")
            res = filtrar_productos_por_marca(productos, marca)
            imprimir_lista_productos(res)
        elif opcion == '4':
            cat = input("Categoría: ")
            cantidad = contar_productos_por_categoria(productos, cat)
            print(f"Hay {cantidad} producto(s) en la categoría '{cat}'.")
        elif opcion == '0':
            break
        else:
            print("Opción inválida.")

def submenu_avanzado():
    print("""
-- Búsqueda avanzada --
Puede combinar criterios. Deje en blanco lo que no aplique.
""")
    nombre = input("Nombre: ")
    marca = input("Marca: ")
    categoria = input("Categoría: ")
    min_precio = input("Mínimo precio: ")
    max_precio = input("Máximo precio: ")
    disponible = input("Disponible (s/n): ").strip().lower()
    min_stock = input("Mínimo stock: ")

    criterios = {}
    if nombre: criterios['nombre'] = nombre
    if marca: criterios['marca'] = marca
    if categoria: criterios['categoria'] = categoria
    if min_precio: criterios['min_precio'] = float(min_precio)
    if max_precio: criterios['max_precio'] = float(max_precio)
    if disponible in ('s','n'): criterios['disponible'] = (disponible == 's')
    if min_stock: criterios['min_stock'] = int(min_stock)

    operador = input("Operador (AND/OR) [AND]: ").strip().upper() or 'AND'

    usar_aprox = input("Usar coincidencia aproximada en nombre/marca (s/n)? [n]: ").strip().lower() or 'n'
    aprox = None
    if usar_aprox == 's':
        try:
            tol = int(input("Tolerancia (entero, recomendado 1-2): ").strip())
        except ValueError:
            tol = 1
        aprox = {'nombre': tol, 'marca': tol}

    res = buscar_productos_avanzado(productos, criterios, operador=operador, aproximado=aprox)
    imprimir_lista_productos(res)


if __name__ == "__main__":
    menu_principal()
