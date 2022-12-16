Console.Clear();
int[] a = {1, 2, 3, 4, 5};
int[] b = new int[a.Length];
for (int i = 0; i < a.Length; i++)  // Правильное копирование по элементно, если написать b = a, то это ссылка b на a
    b[i] = a[i];

b[0] = -1;
Console.WriteLine(string.Join(" ", a));
Console.WriteLine(string.Join(" ", b));
