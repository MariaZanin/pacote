while True:
    try:
        numero=int(input('Entre com um número INT: '))
        print(5/numero)
        break
    except (ValueError, ZeroDivisionError):
        print('Valor errado ou Não é possível dividir por zero.')
    except:
        print('Desculpe, algo errado aconteceu...')