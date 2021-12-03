try : #tenta isso
    a = int(input("Número 1: "))
    b = int(input("Número 2: "))
    div = a / b
#except Exception as erro: #se der errado
    #print(f"Problema... Causa: {erro.__class__}")

except (ValueError, TypeError):
    print("Tipos de dados inválidos!")
except ZeroDivisionError:
    print("Impossível fazer divisão por zero!")
except KeyboardInterrupt: #caso cancele a execução 
    print("Não foi digitado nenhum valor!")

else: #se der certo
    print(f"Resultado: {div:.2f}")

finally:
    print("Xama meu consagrado é nois, um abraço! ")
