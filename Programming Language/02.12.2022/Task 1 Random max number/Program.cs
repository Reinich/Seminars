Console.Clear();

int n = new Random().Next(10, 100); // Последнее число не включительно, то есть от 10 до 99
Console.WriteLine("Рандомное число: " + n);
int max;
int a = n % 10;
int b = n / 10;

if (a > b)
{
    max = a;
}
else max = b;

Console.WriteLine("Его максимальное число: " + max);