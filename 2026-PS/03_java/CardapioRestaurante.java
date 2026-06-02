import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Locale localeBR = Locale.forLanguageTag("pt-BR");
        DecimalFormatSymbols symbols = new DecimalFormatSymbols(localeBR);
        symbols.setDecimalSeparator(',');
        DecimalFormat moeda = new DecimalFormat("#,##0.00", symbols);

        System.out.println("=================================");
        System.out.println("     CARDÁPIO ELETRÔNICO");
        System.out.println("=================================");
        System.out.println("1 - X-Burguer .......... R$ 18,00");
        System.out.println("2 - Pizza .............. R$ 35,00");
        System.out.println("3 - Suco Natural ....... R$ 8,00");
        System.out.println("4 - Café ............... R$ 5,00");
        System.out.println("5 - Batata ............... R$ 2,50");
        System.out.println("=================================");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        String item = "";
        double precoUnitario = 0.0;

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
                System.out.println("Opção inválida.");
                entrada.close();
                return;
        }

        System.out.print("Quantidade desejada: ");
        int quantidade = entrada.nextInt();

        if (quantidade <= 0) {
            System.out.println("Quantidade inválida. O valor deve ser maior que zero.");
            entrada.close();
            return;
        }

        double total = precoUnitario * quantidade;

        System.out.println("\n===== RESUMO DO PEDIDO =====");
        System.out.println("Item: " + item);
        System.out.println("Preço unitário: R$ " + moeda.format(precoUnitario));
        System.out.println("Quantidade: " + quantidade);
        System.out.println("Valor total: R$ " + moeda.format(total));
        System.out.println("============================");

        entrada.close();
    }
}