import java.util.ArrayList;

public class ConsolidaçãoF {

    // Exercício 1 - somar todos os itens de um array
    // Recebe um array de inteiros e retorna a soma de todos os elementos.
    static int somarTudo(int[] numeros) {
        int total = 0;
        for (int i = 0; i < numeros.length; i++) {
            total = total + numeros[i];
        }
        return total;
    }

    // Exercício 2 (parcial) - contar elementos maiores que um limite
    // Recebe um array de inteiros e um limite, retorna quantos valores são maiores que esse limite.
    static int contarAcima(int[] valores, int limite) {
        int quantidade = 0;
        for (int v : valores) {
            if (v > limite) {
                quantidade = quantidade + 1;
            }
        }
        return quantidade;
    }

    // Exercício 4 - maior valor de um array
    // Percorre o array e guarda o maior valor encontrado.
    static int maiorValor(int[] valores) {
        int maiorAteAgora = valores[0];
        for (int v : valores) {
            if (v > maiorAteAgora) {
                maiorAteAgora = v;
            }
        }
        return maiorAteAgora;
    }

    // Exercício 4 - maior valor entre dois números (sobrecarga)
    // Retorna o maior dos dois valores inteiros.
    static int maiorValor(int a, int b) {
        return a > b ? a : b;
    }

    // Calcula a média de um array de inteiros usando o método somarTudo
    static double media(int[] numeros) {
        int total = somarTudo(numeros);
        return (double) total / numeros.length;
    }

    // Exercício 5 / 1 - calcular a média de um array de notas double
    // Reutiliza array + laço para calcular a média.
    static double calcularMedia(double[] notas) {
        double soma = 0.0;
        for (int i = 0; i < notas.length; i++) {
            soma += notas[i];
        }
        return soma / notas.length;
    }

    // Exercício 2 - contar aprovados
    // Retorna quantas notas são maiores ou iguais a 6.0.
    static int contarAprovados(double[] notas) {
        int quantidade = 0;
        for (double nota : notas) {
            if (nota >= 6.0) {
                quantidade = quantidade + 1;
            }
        }
        return quantidade;
    }

    // Exercício 5 - exibir boletim integrador
    // Reaproveita calcularMedia e contarAprovados para mostrar média, aprovados e situação.
    static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        String situacao = media >= 6.0 ? "APROVADA" : "EM RECUPERACAO";

        System.out.println("Media: " + media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Situacao: " + situacao);
    }

    // Conta quantos valores estão acima da média de um array de inteiros
    // Combina cálculo de média com loop condicional.
    static int contarAcimaDaMedia(int[] valores) {
        double media = media(valores);
        int quantidade = 0;
        for (int v : valores) {
            if (v > media) {
                quantidade = quantidade + 1;
            }
        }
        return quantidade;
    }

    // Exercício 3 - adicionar produto em ArrayList
    // Recebe uma lista e um nome e adiciona o item à lista.
    static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    // Exercício 3 - listar produtos numerados
    // Percorre a lista e exibe cada item com seu número de ordem.
    static void listarProdutos(ArrayList<String> lista) {
        int numero = 1;
        for (String item : lista) {
            System.out.println(numero + " - " + item);
            numero = numero + 1;
        }
    }

    public static void main(String[] args) {
        // Teste do exercício 1: soma dos elementos do array
        int[] valores = {10, 20, 30};
        System.out.println(somarTudo(valores)); // 60

        // Teste do exercício 2 parcial: contar valores acima de 50
        int[] notas = {40, 75, 90, 30};
        System.out.println(contarAcima(notas, 50)); // 2

        // Teste do exercício 4: maior valor em array
        int[] idades = {17, 23, 15, 31};
        System.out.println(maiorValor(idades)); // 31

        // Testes de sobrecarga do exercício 4
        System.out.println(maiorValor(new int[]{3, 9, 5})); // 9
        System.out.println(maiorValor(12, 7)); // 12
        System.out.println(maiorValor(new int[]{4, 4, 4})); // 4

        // Teste de média e contar acima da média
        int[] numeros = {10, 20, 30};
        System.out.println(media(numeros)); // 20.0
        System.out.println(contarAcimaDaMedia(numeros)); // 1

        // Exercício 1 / 5: calcular média de notas double
        double[] notas1 = {7.0, 8.0, 9.0};
        System.out.println(calcularMedia(notas1)); // 8.0

        double[] notas2 = {6.0, 6.0, 6.0, 6.0};
        System.out.println(calcularMedia(notas2)); // 6.0

        double[] notas3 = {5.0, 10.0};
        System.out.println(calcularMedia(notas3)); // 7.5

        // Exercício 2: contar aprovados
        double[] aprovados1 = {7.0, 4.0, 9.0, 6.0};
        System.out.println(contarAprovados(aprovados1)); // 3

        double[] aprovados2 = {2.0, 3.0, 5.0};
        System.out.println(contarAprovados(aprovados2)); // 0

        double[] aprovados3 = {10.0, 8.0, 6.0};
        System.out.println(contarAprovados(aprovados3)); // 3

        // Exercício 5: boletim integrador
        double[] boletim1 = {7.0, 5.0, 9.0, 6.0};
        exibirBoletim(boletim1);
        // Esperado:
        // Media: 6.75
        // Aprovados: 3
        // Situacao: APROVADA

        double[] boletim2 = {4.0, 3.0, 5.0};
        exibirBoletim(boletim2);
        // Esperado:
        // Media: 4.0
        // Aprovados: 0
        // Situacao: EM RECUPERACAO

        // Exercício 3: catálogo de produtos
        ArrayList<String> produtos = new ArrayList<>();
        adicionarProduto(produtos, "Pizza");
        adicionarProduto(produtos, "Suco");
        listarProdutos(produtos);
    }
}
