static int menorValor(int[] numeros) {
    int menor = numeros[0];
    int it = 1;
    while (it < numeros.length) {
        if (numeros[it] < menor) {
            menor = numeros[it];
        }
        it++;
    }
    return menor;
}