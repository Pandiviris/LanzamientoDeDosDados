#Simulando lanzamiento de dos dados. Realizado por Jose Diaz y Ashly Scarpati. Simulacion y modelos UDONE
import random

def main():
    print("\nSimulando lanzamiento de dos dados de seis lados")
    print("\n=====================")
    print("\nRealizado por Jose Diaz y Ashly Scarpati")
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