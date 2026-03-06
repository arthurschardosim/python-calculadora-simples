"""
Calculadora Simples
"""

def calcular(num1: float, num2: float, operacao: str):
    match operacao:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                raise ValueError("Divisão por zero não é permitida.")
            return num1 / num2
        case _:
            raise ValueError("Operação inválida. Use +, -, * ou /.")


def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        resultado = calcular(num1, num2, operacao)

        print(f"Resultado: {resultado}")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()