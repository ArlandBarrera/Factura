# V 1.0
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
    print(f"Impuesto sobre producto: {itbms}%")
    print("-" * caracteres)
    print("Precio\t-\tImpuesto\t-\tTotal")
    print("-" * caracteres)
    for i, precio in enumerate(precios):
        total_producto = precio + impuesto[i]
        monto_total += total_producto
        impuesto[i] = round(impuesto[i], 4)
        total_producto = round(total_producto, 2)
        print(
            f"{precio/cantidad[i]}x{cantidad[i]}\t-\t{impuesto[i]}\t-\t{total_producto}"
        )
        print("-" * caracteres)
    monto_total = round(monto_total, 2)
    print(f"Monto Total: {monto_total}")


def main():
    precios_productos = []
    impuesto_productos = []
    cantidades_productos = []
    opcion = ""
    cantidad_caracteres = 45
    print("CALCULADORA DE IMPUESTOS Y PRECIO TOTAL V 1.0")
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
