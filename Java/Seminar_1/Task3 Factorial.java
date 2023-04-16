import java.util.Scanner;
public class Task3 {
    public static void main(String[] args) {
        /* Вводится натуральное число n. Вычислите n! ("эн-факториал") */

        Scanner readTerminal = new Scanner(System.in);
        System.out.printf("n: ");
        int n = readTerminal.nextInt();
        int f = 1;
        for (int i = 1; i <= n; i++) {
            f *= i;

        }
        System.out.println(f);
        readTerminal.close();
    }
}
