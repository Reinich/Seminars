Console.Clear();

Console.Write("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());

if (n%7==0 && n%23==0) Console.WriteLine("Это число кратно и 7, и 23");
else Console.WriteLine("Это число не кратно 7 и 23 одновременно");



