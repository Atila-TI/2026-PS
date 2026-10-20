public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean resultado = dao.adicionarLivro(
            "Dom Casmurro",
            "Machado de Assis",
            1899
        );

        System.out.println(
            "Livro adicionado: " + resultado
        );
    }
}