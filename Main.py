#Simulando lanzamiento de dos dados. Realizado por Jose Diaz CI 26586272 y Ashly Scarpati CI 27424492. Simulacion y modelos UDONE
import random

def main():
    print("\nSimulando lanzamiento de dos dados de seis lados")
    print("\n=====================")
    print("\nRealizado por Jose Diaz CI 26586272 y Ashly Scarpati CI 27424492.")
    print("\n=====================")
    sw = "1"
    while sw=="1":        
        for i in range(1,3):            
            random.seed(None)
            resultado = random.randint(1, 6)
            print("el resultado de su", i,"dado es ", resultado)
            
        print("Ingrese 1 si desea lanzar otro par de dados de seis lados")
        sw = input()


if __name__ == "__main__":
    main()