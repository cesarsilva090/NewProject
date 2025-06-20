// LoginSimples.java

import java.util.Scanner;

public class LoginSimples {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String usuarioCerto = "admin";
        String senhaCerta = "1234";

        System.out.print("Usuário: ");
        String usuario = input.nextLine();

        System.out.print("Senha: ");
        String senha = input.nextLine();

        if (usuario.equals(usuarioCerto) && senha.equals(senhaCerta)) {
            System.out.println("Login bem-sucedido!");
        } else {
            System.out.println("Usuário ou senha incorretos.");
        }

        input.close();
    }
}
