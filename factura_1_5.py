# V 1.5
import time

colors = {
    "r": "\033[31m",
    "v": "\033[32m",
    "m": "\033[33m",
    "z": "\033[34m",
    "c": "\033[36m",
    "n": "\033[0m",
}


def cnv_str_float_try(string):
    try:
        float(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo valores numericos.{colors['n']}")


def cnv_str_int_try(string):
    try:
        int(string)
        return True
    except ValueError:
        print(f"{colors['r']}Computo no valido. Solo numeros enteros.{colors['n']}")


def num_myr_cero(num, indicacion):
    if num <= 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser cero o negativo.{colors['n']}"
        )
        return False
    return True


def num_neg(num, indicacion):
    if num < 0:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser negativo.{colors['n']}"
        )
        return False
    return True


def num_myr_cien(num, indicacion):
    if num > 100:
        print(
            f"{colors['r']}El valor `{indicacion}` no puede ser mayor a cien.{colors['n']}"
        )
        return False
    return True


def cnv_str_int_cero(string, indicacion):
    if cnv_str_int_try(string):
        num = int(string)
        if num_myr_cero(num, indicacion):
            return True
    return False


def cnv_str_float_cero(string, indicacion):
    if cnv_str_float_try(string):
        num = float(string)
        if num_myr_cero(num, indicacion):
            return True
    return False


def cnv_str_float_neg(string, indicacion):
    if cnv_str_float_try(string):
        num = float(string)
        if num_neg(num, indicacion):
            return True
    return False


def cnv_str_descuento(string, indicacion):
    if cnv_str_float_try(string):
        num = float(string)
        if num_neg(num, indicacion) and num_myr_cien(num, indicacion):
            return True
    return False


def clc_cnt(precio, cantidad):
    precio_cantidad = precio * cantidad
    return precio_cantidad


def clc_imp(precio, cantidad, impuesto):
    valor_impuesto = clc_cnt(precio, cantidad) * impuesto
    return valor_impuesto


def calcular_descuento(precio, porcentaje_descuento):
    porcentaje_descuento = float(porcentaje_descuento)
    descuento = porcentaje_descuento / 100
    precio_descontado = precio * (1 - descuento)
    return precio_descontado


def mostrar_resultados(precio, cantidad, impuesto, total):
    print(f"{(precio):.2f}x{cantidad}\t-\t{(impuesto):.2f}\t-\t{(total):.2f}")


def factura(precios, cantidad, iva, itbms, descuentos, caracteres):
    monto_total = 0
    impuesto_precontado = 0
    total_precontado = 0
    tasa_descuento = 0
    print("-" * caracteres)
    print("\t\tFACTURA")
    print("-" * caracteres)
    print(f"Fecha: {time.asctime(time.localtime(time.time()))}")
    print("-" * caracteres)
    print(f"Impuesto sobre producto: {iva}%")
    print("-" * caracteres)
    print("Precio\t-\tImpuesto\t-\tTotal")
    print("-" * caracteres)
    for i, precio in enumerate(precios):
        precio_producto = precio
        if i in descuentos:
            tasa_descuento, precio_producto = descuentos[i]
            impuesto_precontado = clc_imp(precio, cantidad[i], itbms)
            total_precontado = clc_cnt(precio, cantidad[i]) + impuesto_precontado
        impuesto = clc_imp(precio_producto, cantidad[i], itbms)
        total_producto = clc_cnt(precio_producto, cantidad[i]) + impuesto
        monto_total += total_producto
        if i in descuentos:
            print(f"{colors['r']}Predescuento{colors['n']}")
            mostrar_resultados(
                precio, cantidad[i], impuesto_precontado, total_precontado
            )
            print(
                f"{colors['z']}Descuento {colors['c']}({tasa_descuento}%){colors['n']}"
            )
            mostrar_resultados(precio_producto, cantidad[i], impuesto, total_producto)
            print(f"{colors['m']}Ahorro{colors['n']}")
            mostrar_resultados(
                precio - precio_producto,
                cantidad[i],
                impuesto_precontado - impuesto,
                total_precontado - total_producto,
            )
        else:
            mostrar_resultados(precio_producto, cantidad[i], impuesto, total_producto)
        print("-" * caracteres)
    monto_total = f"{round(monto_total, 2):.2f}"
    print(f"Monto Total: {monto_total}")


def main():
    precios_productos = []
    cantidades_productos = []
    descuentos = {}
    opcion = ""
    cantidad_caracteres = 45
    print("-" * cantidad_caracteres)
    print("CALCULADORA DE IMPUESTOS Y PRECIO TOTAL V 1.5")
    print("-" * cantidad_caracteres)
    # Impuesto de Consumo
    # VAT - Value Added Tax
    # IVA - Impuesto de Valor Agregado
    # En Panama es llamaado ITBMS
    # Impuesto a las Transferencias de Bienes Corporales Muebles
    # y la Prestacion de Servicios
    iva = input("Tasa de impuesto (%): ")
    while not cnv_str_float_neg(iva, "tasa de impuesto"):
        iva = input("Tasa de impuesto (%): ")
    itbms = float(iva) / 100
    while opcion != "0":
        print("*" * cantidad_caracteres)
        print(f"{colors['m']}Producto{colors['n']}")
        precio = input("Precio: ")
        while not cnv_str_float_cero(precio, "precio de producto"):
            precio = input("Precio: ")
        precio = float(precio)
        cantidad = input("Cantidad: ")
        while not cnv_str_int_cero(cantidad, "cantidad de producto"):
            cantidad = input("Cantidad: ")
        cantidad = int(cantidad)
        cantidades_productos.append(cantidad)
        precios_productos.append(precio)
        print(f"{colors['z']}Descuento{colors['n']}")
        print(f"{colors['r']}No -> 0{colors['n']}")
        print(f"{colors['v']}Si -> 1{colors['n']}")
        opcion_descuento = input("-> ")
        while opcion_descuento not in ["0", "1"]:
            print(f"{colors['r']}Disyuntiva no aceptable.{colors['n']}")
            print(f"{colors['z']}Descuento{colors['n']}")
            print(f"{colors['r']}No -> 0{colors['n']}")
            print(f"{colors['v']}Si -> 1{colors['n']}")
            opcion_descuento = input("-> ")
        if opcion_descuento == "1":
            porcentaje_descuento = input("Tasa de descuento (%): ")
            while not cnv_str_descuento(porcentaje_descuento, "tasa de descuento"):
                porcentaje_descuento = input("Tasa de descuento (%): ")
            descuentos.update(
                {
                    (len(precios_productos) - 1): (
                        porcentaje_descuento,
                        calcular_descuento(precios_productos[-1], porcentaje_descuento),
                    )
                }
            )
        print("+" * cantidad_caracteres)
        print(f"{colors['r']}Salir -> 0{colors['n']}")
        print(f"{colors['v']}Agregar producto -> 1{colors['n']}")
        opcion = input("-> ")
        while opcion not in ["0", "1"]:
            print(f"{colors['r']}Disyuntiva no aceptable.{colors['n']}")
            print(f"{colors['r']}Salir -> 0{colors['n']}")
            print(f"{colors['v']}Agregar producto -> 1{colors['n']}")
            opcion = input("-> ")
    print("\n")
    factura(
        precios_productos,
        cantidades_productos,
        iva,
        itbms,
        descuentos,
        cantidad_caracteres,
    )


if __name__ == "__main__":
    main()
