Console.Clear();

Console.Write("Введите X: ");
double x = Convert.ToDouble(Console.ReadLine());

Console.Write("Введите Y: ");
double y = Convert.ToDouble(Console.ReadLine());

while (x == 0)
{
    Console.Write("Вы ошиблись. \n Введите новую X координату: ");
    x = Convert.ToDouble(Console.ReadLine());
}

while (y == 0)
{
    Console.Write("Вы ошиблись. \n Введите новую Y координату: ");
    y = Convert.ToDouble(Console.ReadLine());
}

if (x > 0 && y > 0) Console.Write("Это первая четверть");
else if (x < 0 && y > 0) Console.Write("Это вторая четверть");
else if (x < 0 && y < 0) Console.Write("Это третья четверть");
else Console.Write("Это четвертая четверть");
