# V 1.4

import time


def convertir_string_float_try(string):
    try:
        float(string)
        return True
    except ValueError:
        print("Computo no valido. Solo valores numericos.")


def convertir_string_int_try(string):
    try:
        int(string)
        return True
    except ValueError:
        print("Computo no valido. Solo numeros enteros.")


def calcular_impuesto(precio, impuesto):
    valor_impuesto = precio * impuesto
    return valor_impuesto


def filtrar_string_int(string, indicacion):
    while not convertir_string_int_try(string) or string == "0":
        if string == "0":
            print(f"{indicacion} no puede ser cero.")
        return False
    return True


def filtrar_string_float(string, indicacion):
    while not convertir_string_float_try(string) or string == "0":
        if string == "0":
            print(f"{indicacion} no puede ser cero.")
        return False
    return True


def factura(precios, impuesto, cantidad, itbms, caracteres):
    monto_total = 0
    print("-" * caracteres)
    print("\t\tFACTURA")
    print("-" * caracteres)
    print(f"Fecha: {time.asctime(time.localtime(time.time()))}")
    print("-" * caracteres)
    print(f"Impuesto sobre producto: {itbms}%")
    print("-" * caracteres)
    print("Precio\t-\tImpuesto\t-\tTotal")
    print("-" * caracteres)
    for i, precio in enumerate(precios):
        total_producto = precio + impuesto[i]
        monto_total += total_producto
        impuesto[i] = f"{round(impuesto[i], 2):.2f}"
        total_producto = f"{round(total_producto, 2):.2f}"
        print(
            f"{(precio/cantidad[i]):.2f}x{cantidad[i]}\t-\t{impuesto[i]}\t-\t{total_producto}"
        )
        print("-" * caracteres)
    monto_total = f"{round(monto_total, 2):.2f}"
    print(f"Monto Total: {monto_total}")


def main():
    precios_productos = []
    impuesto_productos = []
    cantidades_productos = []
    opcion = ""
    cantidad_caracteres = 45
    print("-" * cantidad_caracteres)
    print("CALCULADORA DE IMPUESTOS Y PRECIO TOTAL V 1.4")
    print("-" * cantidad_caracteres)
    # Impuesto de Consumo
    # VAT - Value Added Tax
    # IVA - Impuesto de Valor Agregado
    # En Panama es llamaado ITBMS
    # Impuesto a las Transferencias de Bienes Corporales Muebles
    # y la Prestacion de Servicios
    iva = input("Tasa de impuesto (%): ")
    while not filtrar_string_float(iva, "La tasa de impuesto"):
        iva = input("Tasa de impuesto (%): ")
    itbms = float(iva) / 100
    print("-" * cantidad_caracteres)
    while opcion != "0":
        print()
        print("*" * cantidad_caracteres)
        precio = input("Precio de producto: ")
        while not filtrar_string_float(precio, "El precio del producto"):
            precio = input("Precio de Producto: ")
        precio = float(precio)
        cantidad = input("Cantidad: ")
        while not filtrar_string_int(cantidad, "La cantidad"):
            cantidad = input("Cantidad: ")
        cantidad = int(cantidad)
        cantidades_productos.append(cantidad)
        precio *= cantidad
        precios_productos.append(precio)
        impuesto = calcular_impuesto(precio, itbms)
        impuesto_productos.append(impuesto)
        print("*" * cantidad_caracteres)
        print()
        print("+" * cantidad_caracteres)
        print("Salir -> 0")
        print("Agregar producto -> 1")
        opcion = input("-> ")
        while opcion not in ["0", "1"]:
            print("\nDisyuntiva no aeptable\n")
            print("Salir -> 0")
            print("Agregar producto -> 1")
            opcion = input("-> ")
        print("+" * cantidad_caracteres)
    print("\n")
    factura(
        precios_productos,
        impuesto_productos,
        cantidades_productos,
        iva,
        cantidad_caracteres,
    )


if __name__ == "__main__":
    main()
