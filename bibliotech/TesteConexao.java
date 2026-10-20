import java.sql.Connection;
import java.sql.SQLException;

public class TesteConexao {

    public static void main(String[] args) {

        try (Connection conexao =
                Conexao.conectar()) {

            if (!conexao.isValid(2)) {
                throw new SQLException("A conexão com o banco não é válida.");
            }

            System.out.println(
                "Conexão realizada com sucesso!"
            );

            System.out.println(
                "Banco: bibliotech"
            );

        } catch (SQLException e) {

            System.out.println(
                "Erro ao conectar ao banco."
            );

            System.out.println(
                e.getMessage()
            );
        }
    }
}