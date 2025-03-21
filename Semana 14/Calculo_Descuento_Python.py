def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (int, optional): El porcentaje de descuento a aplicar. Defaults to 10.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = (porcentaje_descuento / 100) * monto_total
    return descuento

# Llamadas de ejemplo
monto_compra1 = 100.00
descuento1 = calcular_descuento(monto_compra1)
print(f"Monto total: ${monto_compra1}, Descuento (10%): ${descuento1}, Monto con descuento: ${monto_compra1 - descuento1}")

monto_compra2 = 250.00
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
print(f"Monto total: ${monto_compra2}, Descuento (20%): ${descuento2}, Monto con descuento: ${monto_compra2 - descuento2}")