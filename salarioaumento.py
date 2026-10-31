salario_atual = float(input("Digite o salário atual (R$): "))
percentual_aumento = float(input("Digite o percentual de aumento (%): "))
percentual_desconto = float(input("Digite o percentual de desconto (%): "))

# 1. Aplica o aumento primeiro
valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

# 2. Aplica o desconto sobre o novo salário
valor_desconto = novo_salario * (percentual_desconto / 100)
salario_final = novo_salario - valor_desconto

# Exibe o relatório de forma organizada
print("\n" + "="*30)
print("     RELATÓRIO SALARIAL     ")
print("="*30)
print(f"Salário antes do aumento : R$ {salario_atual:.2f}")
print(f"Valor do aumento ({percentual_aumento}%) : R$ {valor_aumento:.2f}")
print(f"Novo salário (com aumento): R$ {novo_salario:.2f}")
print(f"Valor do desconto ({percentual_desconto}%): R$ {valor_desconto:.2f}")
print(f"Salário final a receber  : R$ {salario_final:.2f}")
print("="*30)
