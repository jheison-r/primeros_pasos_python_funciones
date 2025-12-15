def obtener_transaccion():
    tipo = input("Digite tipo de transacción (D depósito / R retiro / FIN): ")
    return tipo


def procesar_transacciones():
    saldo = 1000
    contador = 0

    while True:
        tipo = obtener_transaccion()

        if tipo == "FIN":
            break

        monto = float(input("Digite el monto: "))

        if tipo == "D":
            saldo += monto
            contador += 1

        elif tipo == "R":
            if saldo - monto >= 0:
                saldo -= monto
                contador += 1
            else:
                print("Fondos insuficientes")

    return saldo, contador


def mostrar_resultado(saldo, contador):
    print("Saldo final:", saldo)
    print("Transacciones válidas:", contador)


# *********** zona de código principal ***********

saldo_final, total = procesar_transacciones()
mostrar_resultado(saldo_final, total)