public class Task5 {
    /*
     * Заданы три целых числа а, b, с, где a > b
     * Sample Input:
     * 20
     * 1
     * 2
     * Sample Output:
     * 20
     * 18
     * 16
     * 14
     * 12
     * 10
     * 8
     * 6
     * 4
     * 2
     */
    public static void main(String[] args) {
        int b = 1;
        int c = 2;
        for (int a = 20; a > b; a -= c)
            System.out.println(a);
    }

}
