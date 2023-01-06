Console.Clear();

int n = new Random().Next(100, 1000); // Последнее число не включительно, то есть от 10 до 99
Console.WriteLine($"Рандомное число: {n}"); // Такая запись более верная

int m1 = n/100;
int m2 = n%10;
Console.Write($"Число без середины: {m1}");
Console.WriteLine(m2);
