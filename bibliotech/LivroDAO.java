import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class LivroDAO {

    public boolean adicionarLivro(
        String titulo,
        String autor,
        int ano) {

    String sql =
        "INSERT INTO livros (titulo, autor, ano) " +
        "VALUES (?, ?, ?)";

    try (Connection conexao = Conexao.conectar();
         PreparedStatement comando =
             conexao.prepareStatement(sql)) {

        comando.setString(1, titulo);
        comando.setString(2, autor);
        comando.setInt(3, ano);

        int linhas = comando.executeUpdate();

        return linhas > 0;

    } catch (SQLException e) {

        System.out.println(
            "Erro ao adicionar livro: " +
            e.getMessage()
        );

        return false;
    }
}

}