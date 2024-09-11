# V 1.3

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


def factura(precios, impuesto, cantidad, itbms, caracteres):
    monto_total = 0
    print("-" * caracteres)
    print("\t\tFACTURA")
    print("-" * caracteres)
    # V 1.3
    # Mostrar fecha local
    print(f"Fecha: {time.asctime(time.localtime(time.time()))}")
    print("-" * caracteres)
    print(f"Impuesto sobre producto: {itbms}%")
    print("-" * caracteres)
    print("Precio\t-\tImpuesto\t-\tTotal")
    print("-" * caracteres)
    for i, precio in enumerate(precios):
        total_producto = precio + impuesto[i]
        monto_total += total_producto
        # V 1.1
        # Formateo de valores para mostrar siempre decimales fijos
        # dos decimales para el precio y total del producto, y monto total
        # cuatro decimales para el impuesto
        # V 1.2
        # EL impuesto tiene dos decimales
        # el impuesto es una cantidad monetaria -> dolares y centavos
        # TODO
        # el impuesto sobre uno o muchos productos se puede factorizar
        # sum(precio_todos_los_productos) * tasa_de_impuesto
        # A*r + B*r + C*r = (A+B+C)*r
        # dos opciones:
        # mostrar impuesto por producto (actual)
        # mostar impuesto total (futura opcion)
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
    print("CALCULADORA DE IMPUESTOS Y PRECIO TOTAL V 1.3")
    print("-" * cantidad_caracteres)
    # Impuesto de Consumo
    # VAT - Value Added Tax
    # IVA - Impuesto de Valor Agregado
    # En Panama es llamaado ITBMS
    # Impuesto a las Transferencias de Bienes Corporales Muebles
    # y la Prestacion de Servicios
    iva = input("Tasa de impuesto (%): ")
    while not convertir_string_float_try(iva):
        iva = input("Tasa de impuesto (%): ")
    itbms = float(iva) / 100
    print("-" * cantidad_caracteres)
    while opcion != "0":
        print()
        print("*" * cantidad_caracteres)
        precio = input("Precio de producto: ")
        while not convertir_string_float_try(precio):
            precio = input("Precio de Producto: ")
        precio = float(precio)
        cantidad = input("Cantidad: ")
        while not convertir_string_int_try(cantidad) or cantidad == "0":
            if cantidad == "0":
                print("La cantidad no puede ser cero.")
            cantidad = input("Cantidad: ")
        cantidad = int(cantidad)
        while cantidad == 0:
            print("La cantidad no puede ser cero.")
        cantidades_productos.append(cantidad)
        precio *= cantidad
        precios_productos.append(precio)
        impuesto = calcular_impuesto(precio, itbms)
        impuesto_productos.append(impuesto)
        print("*" * cantidad_caracteres)
        print()
        print("+" * cantidad_caracteres)
        print("Salir -> 0")
        print("Otro producto -> Cualquier otra  cosa")
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
