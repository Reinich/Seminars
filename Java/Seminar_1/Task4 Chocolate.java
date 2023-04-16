public class Task4 {
    public static void main(String[] args) {
        /*
         * Требуется определить, можно ли от шоколадки размером n × m долек отломить k
         * долек,
         * если разрешается сделать один разлом по прямой между дольками (то есть
         * разломить
         * шоколадку на два прямоугольника).
         * Входные данные
         * Вводятся 3 числа: n, m и k; k не равно n × m. Гарантируется, что количество
         * долек в шоколадке не превосходит 30000.
         * Выходные данные
         * Программа должна вывести слово YES, если возможно отломить указанное число
         * долек,
         * в противном случае вывести слово NO.
         * Sample Input 1:
         * 3 2 4
         * Sample Output 1:
         * YES
         */
        Scanner readTerminal = new Scanner(System.in);
        System.out.printf("n: ");
        int n = readTerminal.nextLine();
        System.out.printf("m: ");
        int m = readTerminal.nextLine();
        System.out.printf("k: ");
        int k = readTerminal.nextLine();
        
        readTerminal.close();
    }
}
