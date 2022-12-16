Console.Clear();
Console.Write("Введите число: ");
int n = Convert.ToInt32(Console.ReadLine());
string result = string.Empty;
while (n > 0)
{
    result = result + Convert.ToString(n % 2); // result = Convert.ToString(n % 2) + result; Переворот
    n /= 2;
}
Console.WriteLine(result);