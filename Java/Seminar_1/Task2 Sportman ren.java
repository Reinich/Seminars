import java.util.Scanner;

public class Task2 {
    public static void main(String[] args) {
        /*
         * В первый день спортсмен пробежал x километров, а затем он каждый день
         * увеличивал пробег
         * на 10% от предыдущего значения. По данному числу y определите номер дня, на
         * который пробег спортсмена составит не менее y километров.
         * Программа получает на вход действительные числа x и y
         * Sample Input:
         * 10
         * 20
         * Sample Output:
         * 9
         */
        Scanner readTerminal = new Scanner(System.in);
        System.out.printf("x: ");
        double x = readTerminal.nextInt();
        System.out.printf("y: ");
        double y = readTerminal.nextInt();
        int count = 1;
        while (x <= y) {
            x *= 1.1;
            count++;
        }
        System.out.println(count);

        readTerminal.close();

    }
}
