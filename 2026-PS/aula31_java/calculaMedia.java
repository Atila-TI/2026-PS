static double calculaMedia(int[] numeros) {
    double soma = 0;
    for (int i = 0; i < numeros.length; i++) {
        soma += numeros[i];
    }
    return soma / numeros.length;
}