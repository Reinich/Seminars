Console.Clear();
Console.Write("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());
int f = 1;
for (int i = 2; i <= n; i++)
{
    f = f * i;
    Console.Write(f + " ");
}