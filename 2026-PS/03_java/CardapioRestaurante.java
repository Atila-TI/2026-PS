import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.util.Locale;
import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);

        Locale localeBR = Locale.forLanguageTag("pt-BR");
        DecimalFormatSymbols symbols = new DecimalFormatSymbols(localeBR);
        symbols.setDecimalSeparator(',');
        DecimalFormat moeda = new DecimalFormat("#,##0.00", symbols);

        double totalPedido = 0.0;
        StringBuilder resumoPedido = new StringBuilder();
        boolean continuarComprando = true;

        while (continuarComprando) {
            System.out.println("===========================");
            System.out.println("FAST FOOD IFPR");
            System.out.println("===========================");
            System.out.println("1 - X-Burguer .......... R$ 18,00");
            System.out.println("2 - Pizza .............. R$ 35,00");
            System.out.println("3 - Batata Frita ....... R$ 12,00");
            System.out.println("4 - Refrigerante ....... R$ 8,00");
            System.out.println("5 - Sorvete ............ R$ 10,00");
            System.out.println("6 - Finalizar Pedido");
            System.out.print("\nEscolha: ");
            int opcao = entrada.nextInt();

            String item = "";
            double precoUnitario = 0.0;
            boolean adicionarItem = true;

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
                    item = "Batata Frita";
                    precoUnitario = 12.00;
                    break;
                case 4:
                    item = "Refrigerante";
                    precoUnitario = 8.00;
                    break;
                case 5:
                    item = "Sorvete";
                    precoUnitario = 10.00;
                    break;
                case 6:
                    adicionarItem = false;
                    break;
                default:
                    System.out.println("Opção inválida. Por favor, escolha um número entre 1 e 6.\n");
                    continue;
            }

            if (!adicionarItem) {
                if (totalPedido == 0.0) {
                    System.out.println("Nenhum item foi adicionado ao pedido. Encerrando.");
                    entrada.close();
                    return;
                }
                break;
            }

            System.out.print("\nQuantidade: ");
            int quantidade = entrada.nextInt();

            if (quantidade <= 0) {
                System.out.println("Quantidade inválida. O valor deve ser maior que zero.\n");
                continue;
            }

            double subtotal = precoUnitario * quantidade;
            totalPedido += subtotal;
            resumoPedido.append(quantidade)
                       .append("x ")
                       .append(item)
                       .append(" ........ ")
                       .append("R$ ")
                       .append(moeda.format(subtotal))
                       .append("\n");

            System.out.println("\nItem adicionado ao pedido!\n");
            System.out.println("Deseja continuar comprando?");
            System.out.println("1 - Sim");
            System.out.println("2 - Finalizar");
            System.out.print("\nEscolha: ");
            int continuar = entrada.nextInt();

            if (continuar == 2) {
                continuarComprando = false;
            } else if (continuar != 1) {
                System.out.println("Opção inválida. Finalizando pedido automaticamente.\n");
                continuarComprando = false;
            }

            System.out.println();
        }

        System.out.println("===========================");
        System.out.println("RESUMO DO PEDIDO");
        System.out.println("===========================");
        System.out.print(resumoPedido.toString());
        System.out.println();
        System.out.println("TOTAL: R$ " + moeda.format(totalPedido));
        System.out.println();

        System.out.println("Forma de pagamento:\n");
        System.out.println("1 - Dinheiro");
        System.out.println("2 - Cartão");
        System.out.println("3 - PIX");
        System.out.print("\nEscolha: ");
        int formaPagamento = entrada.nextInt();

        switch (formaPagamento) {
            case 1:
                System.out.println("\nPagamento realizado com sucesso!");
                break;
            case 2:
                System.out.println("\nPagamento realizado com sucesso!");
                break;
            case 3:
                System.out.println("\nPagamento realizado com sucesso!");
                break;
            default:
                System.out.println("\nForma de pagamento inválida. Pedido cancelado.");
                entrada.close();
                return;
        }

        Random random = new Random();
        int numeroPedido = 100 + random.nextInt(900);

        System.out.println();
        System.out.println("Pedido Nº " + numeroPedido);
        System.out.println();
        System.out.println("Aguarde a chamada do seu pedido.");

        entrada.close();
    }
}
