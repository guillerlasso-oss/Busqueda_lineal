"""
datos_ejemplo.py
----------------
Datos de ejemplo para pruebas del sistema "TechStore".
"""

productos = [
    {'id': 1, 'nombre': 'iPhone 15', 'marca': 'Apple', 'categoria': 'Smartphone', 'precio': 999.99, 'stock': 10, 'disponible': True},
    {'id': 2, 'nombre': 'Samsung Galaxy S24', 'marca': 'Samsung', 'categoria': 'Smartphone', 'precio': 899.99, 'stock': 8, 'disponible': True},
    {'id': 3, 'nombre': 'MacBook Air M3', 'marca': 'Apple', 'categoria': 'Laptop', 'precio': 1299.99, 'stock': 5, 'disponible': True},
    {'id': 4, 'nombre': 'Dell XPS 13', 'marca': 'Dell', 'categoria': 'Laptop', 'precio': 1199.99, 'stock': 0, 'disponible': False},
    {'id': 5, 'nombre': 'Sony WH-1000XM5', 'marca': 'Sony', 'categoria': 'Audífonos', 'precio': 399.99, 'stock': 15, 'disponible': True},
    {'id': 6, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablet', 'precio': 599.99, 'stock': 12, 'disponible': True},
    {'id': 7, 'nombre': 'Logitech MX Master 3S', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 119.99, 'stock': 25, 'disponible': True},
    {'id': 8, 'nombre': 'Kindle Paperwhite', 'marca': 'Amazon', 'categoria': 'Lectores', 'precio': 149.99, 'stock': 0, 'disponible': False},
]

empleados = [
    {'id': 101, 'nombre': 'Ana', 'apellido': 'García', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Carlos', 'apellido': 'López', 'departamento': 'Técnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'María', 'apellido': 'Rodríguez', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'José', 'apellido': 'Martínez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
]

print( "========== Productos ============ ")

"=========================================="

print(f"Productos disponibles{productos}")

print("==========================================")


print( "========== Empleados ============ ")


print("==========================================")

print(f"Empleados disponibles{empleados}")