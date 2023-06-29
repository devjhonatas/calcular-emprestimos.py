def verificar_emprestimos(customer):
    loans = []

    if customer["income"] <= 3000:
        loans.append({"type": "Empréstimo pessoal", "taxes": 4})
    elif customer["income"] > 3000 and customer["income"] < 5000:
        if customer["age"] < 30 or customer["location"] == "SP":
            loans.append({"type": "Empréstimo com garantia", "taxes": 3})
    else:
        if customer["age"] < 30 and customer["location"] == "SP":
            loans.append({"type": "Empréstimo com garantia", "taxes": 3})
            loans.append({"type": "Empréstimo consignado", "taxes": 2})

    return loans


def main():
    print("===== Verificador de Empréstimos =====")
    name = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    age = int(input("Digite a idade do cliente: "))
    location = input("Digite a localização do cliente (Ex: SP): ")
    income = float(input("Digite a renda do cliente: "))

    customer = {
        "name": name,
        "cpf": cpf,
        "age": age,
        "location": location,
        "income": income
    }

    # Verificar os tipos de empréstimo adequados
    loans = verificar_emprestimos(customer)

    # Preparar a resposta
    output = {
        "customer": customer["name"],
        "loans": loans
    }

    # Imprimir a resposta
    print("\n===== Resultado =====")
    print("Cliente:", output["customer"])
    print("Tipos de empréstimo adequados:")
    for loan in output["loans"]:
        print("- Tipo:", loan["type"])
        print("  Taxas de juros:", loan["taxes"], "%")


# Executar o programa principal
if __name__ == "__main__":
    main()