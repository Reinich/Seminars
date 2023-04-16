import java.util.Scanner;
class Task1 {
    public static void main(String[] args) {
        /*Улитка ползёт по вертикальному шесту высотой h метров, поднимаясь за день на a метров,
        а за ночь спускаясь на b метров. На какой день улитка доползёт до вершины шеста?
        Программа получает на вход натуральные числа h, a, b. Гарантируется, что a>b.
        */
        Scanner readTerminal = new Scanner(System.in);
        System.out.printf("h: ");
        // int h = Integer.parseInt(model.class.getFromConsole("Введите h"));
        int h = readTerminal.nextInt();
        System.out.printf("a: ");
        int a = readTerminal.nextInt();
        System.out.printf("b: ");
        int b = readTerminal.nextInt();
        int count = 0;
               
        while (h>0) {
            h = h - a;
            if (h < 0) break;
            h += b;
            count++;
        }
        System.out.println(count);
        readTerminal.close();
    }
//     public static void getFromConsole(String msg) {
//         System.out.printf(msg + ": ");
//         Scanner iScanner = new Scanner(System.in);
//         return iScanner.nextInt();
//     } 
}



