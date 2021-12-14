#Simulando lanzamiento de dos dados. Realizado por Jose Diaz CI 26586272 y Ashly Scarpati CI 27424492. Simulacion y modelos UDONE
import random

def main():
    print("\nSimulando lanzamiento de dos dados de seis lados")
    print("\n=====================")
    print("\nRealizado por Jose Diaz CI 26586272 y Ashly Scarpati CI 27424492.")
    print("\n=====================")
    sw = "1"
    while sw=="1":
        print("ingrese cuantos pares de dados desea simular ingrese por ejemplo 1000 o 100")
        simulaciones = int(input())
        listaContadores= crearListaDeContadores()

        for i in range(0,simulaciones):
            dado1 = dado()
            dado2 = dado()
            listaContadores[dado1-1][dado2-1]+=1

        elementoMasRepetido = [0,0,0]
        for i in range(6):
            for j in range(6):
                if (listaContadores[i][j]>elementoMasRepetido[2]):
                    elementoMasRepetido[0]=i
                    elementoMasRepetido[1]=j
                    elementoMasRepetido[2]=listaContadores[i][j]
                
                print("la cantidad de pares de dados con resultados: ",i+1,"y",j+1,"fue de", listaContadores[i][j])
        print("el par de dados que mas se repitio fue",elementoMasRepetido[0]+1,"y",elementoMasRepetido[1]+1, "con un total de ",elementoMasRepetido[2],"repeticiones")

        print("Ingrese 1 si desea repetir la simulacion")
        sw = input()

def dado():
    random.seed(None)
    return random.randint(1, 6)

def crearListaDeContadores():
    listaContadores = [0] * 6
    for i in range(6):
        listaContadores[i] = [0] * 6
    return listaContadores

if __name__ == "__main__":
    main()