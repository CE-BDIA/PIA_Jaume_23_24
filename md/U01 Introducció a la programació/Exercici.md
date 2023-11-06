## 1. Proves de rendiment

En aquesta pràctica anem a fer una prova de rendiment de 3 llenguatges de programació, un compilat com és C, un interpretatm com és Python i un mixte com és Java. 

Tots els programes en qüestió fa la multiplicació de 2 matrius de 2048x2048 elements, amb un total de 8,589,934,592 operacions, combinant multiplicacions i sumes.

Per  la realització del exercici necessitaràs:

- Tenir instal·lat el compilador de C (per defecte a ubuntu)
- Tenir instal·lat un jdk
- Tenir instal·lat Python i la llibreria `numpy`

> És

???+ example "Codi en C"
    ```c
    #include <stdlib.h>
    #include <stdio.h>
    #include <time.h>

    #define n 2048

    double A[n][n];
    double B[n][n];
    double C[n][n];

    int main() {

        //populate the matrices with random values between 0.0 and 1.0
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {

                A[i][j] = (double) rand() / (double) RAND_MAX;
                B[i][j] = (double) rand() / (double) RAND_MAX;
                C[i][j] = 0;
            }
        }

        struct timespec start, end;
        double time_spent;

        //matrix multiplication
        clock_gettime(CLOCK_REALTIME, &start);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }
        clock_gettime(CLOCK_REALTIME, &end);
        time_spent = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1000000000.0;
        printf("Elapsed time in seconds: %f \n", time_spent);
        return 0;
    }
    ```

???+ example "Codi en Python"
    ```python
    import random
    import time

    n = 2048

    #populate the matrices with random values between 0.0 and 1.0
    A = [[random.random() for row in range(n)] for col in range(n)]
    B = [[random.random() for row in range(n)] for col in range(n)]
    C = [[0 for row in range(n)] for col in range(n)]

    start = time.time()
    #matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    end = time.time()
    print("Elapsed time in seconds %0.6f" % (end-start))
    ```

???+ example "Codi en Java"
    ```java
    import java.util.Random;

    public class Matrix{
        static int n = 2048;
        static double[][] A = new double[n][n];
        static double[][] B = new double[n][n];
        static double[][] C = new double[n][n];

        public static void main(String[] args) {
            //populate the matrices with random values between 0.0 and 1.0
            Random r = new Random();
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    A[i][j] = r.nextDouble();
                    B[i][j] = r.nextDouble();
                    C[i][j] = 0;
                }
            }

            long start = System.nanoTime();
            //matrix multiplication
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < n; k++) {
                        C[i][j] += A[i][k] * B[k][j];
                    }
                }
            }

            long stop = System.nanoTime();
            double timeDiff = (stop - start) * 1e-9;
            System.out.println("Elapsed time in seconds: " + timeDiff);
        }
    }
    ```

## 2. Compilació i llanaçament dels programes

1. Compila cada programa (que dega ser compilat) 
2. Executa  5 cops cada programa. 
3. Anota-ho a un full de càlcul, per treure una estadística.

???+ example "Compilació i execució dels programes"
    ```sh
    #C
    gcc MatrixMultiplication.c -o matrix
    ./matrix
    #Java
    javac MatrixMultiplication.java
    java MatrixMultiplication
    #Python
    python MatrixMultiplication.py
    ```

4. Veuras un resultat sorprenenet. Recompila els programes de C així

???+ example "Compilació  optimizada amb C"
    ```sh 
    gcc -O2 MatrixMultiplication.c -o matrixO2
    ./matrix02
    gcc -O3 MatrixMultiplication.c -o matrixO2
    ./matrix03
    ```

## 3. Llibreria d'alt rendiment: `numpy`

Repeteix la prova amb el següent program:

???+ example "Càlcul amb la llibreri `numpy`"
    ```python
    import numpy as np
    import time


    TAM=2048

    #matriu = [[np.random.rand() for j in range(TAM)] for i in range(TAM)]

    m1 = np.random.rand(TAM,TAM)
    m2 = np.random.rand(TAM,TAM)
    desti = np.zeros((TAM,TAM),dtype=float)

    start = time.time()
    nova=np.dot(m1,m2)
    end = time.time()
    print("Amb np: Elapsed time in seconds %0.6f" % (end-start))


    start = time.time()
    #matrix multiplication
    for i in range(TAM):
        for j in range(TAM):
            for k in range(TAM):
                desti[i][j] += m1[i][k] * m2[k][j]
    end = time.time()
    print("Sense np: Elapsed time in seconds %0.6f" % (end-start))
    ```

