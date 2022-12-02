Console.Clear();
Console.Write("Введите первое число ");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число ");
int m = Convert.ToInt32(Console.ReadLine());

if (n * n == m) Console.WriteLine("Одно число является квадратом другого");
else if (m * m == n) Console.WriteLine("Одно число является квадратом другого");
else Console.WriteLine("Числа не являются квадратами друг друга");