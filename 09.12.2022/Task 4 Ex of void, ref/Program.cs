Console.Clear();
void test (ref int a)   // если массив, то по ссылке не передаем, ссылка только для 1 или нескольких значения
{
    a =+5;
}

Console.Write("Введите число");
int n = Convert.ToInt32(Console.ReadLine());
test(ref n);
Console.WriteLine(n);