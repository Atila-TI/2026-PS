import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        // Cria um leitor de entrada para capturar dados do usuário
        Scanner entrada = new Scanner(System.in);

        // Define o locale brasileiro para formatar o valor monetário corretamente
        Locale localeBR = Locale.forLanguageTag("pt-BR");
        DecimalFormatSymbols symbols = new DecimalFormatSymbols(localeBR);
        symbols.setDecimalSeparator(',');

        // Define o formato de moeda com duas casas decimais e separador de vírgula
        DecimalFormat moeda = new DecimalFormat("#,##0.00", symbols);

        // Mostra o cardápio na tela
        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Batata ............... R$ 2,50");
        System.out.println("=================================");

        // Pede para o usuário escolher uma opção do menu
        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        // Variáveis que armazenam o item escolhido e o preço unitário
        String item = "";
        double precoUnitario = 0.0;

        // Seleciona o item correto com base na opção escolhida
        switch (opcao) {
            case 1:
                item = "X-Burguer";
                precoUnitario = 18.00;
                break;
            case 2:
                item = "Pizza";
                precoUnitario = 35.00;
                break;
            case 3:
                item = "Suco Natural";
                precoUnitario = 8.00;
                break;
            case 4:
                item = "Café";
                precoUnitario = 5.00;
                break;
            case 5:
                item = "Batata";
                precoUnitario = 2.50;
                break;
            default:
                // Se a opção não estiver entre 1 e 5, mostra mensagem de erro e encerra
                System.out.println("Opção inválida.");
                entrada.close();
                return;
        }

        // Lê a quantidade desejada pelo usuário
        System.out.print("Quantidade desejada: ");
        int quantidade = entrada.nextInt();

        // Verifica se a quantidade é válida (maior que zero)
        if (quantidade <= 0) {
            System.out.println("Quantidade inválida. O valor deve ser maior que zero.");
            entrada.close();
            return;
        }

        // Calcula o total do pedido multiplicando preço unitário pela quantidade
        double total = precoUnitario * quantidade;

        // Exibe o resumo final do pedido com valores formatados
        System.out.println("\n===== RESUMO DO PEDIDO =====");
        System.out.println("Item: " + item);
        System.out.println("Preço unitário: R$ " + moeda.format(precoUnitario));
        System.out.println("Quantidade: " + quantidade);
        System.out.println("Valor total: R$ " + moeda.format(total));
        System.out.println("============================");

        // Fecha o objeto Scanner para liberar recursos
        entrada.close();
    }
}
