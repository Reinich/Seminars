Console.Clear();

int test(int a, int b)
{
    if (a > b)
        return a;
    return b;
}

Console.Write("Введите 1-ое число");
int n = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите 2-ое число");
int m = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(test(n, m));
// return:
//        - возвращает элемент туда, где была вызвана функция
//        - а также завершает работу функции
//        - Возвращаемое значение необходимо принимать в консоль(ввод) или в переменную нужного типа
//        - Сколько аргументов мы принимает, столько и передаем