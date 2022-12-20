// // double n = new Random().NextDouble() * (end - begin) + begin
// Console.WriteLine(new Random().NextDouble() * (10 + 10) - 10); // [-10, 10]

void InputArray(double[] array)
{
    for (int i = 0; i < array.Length; i++)
        array[i] = Math.Round(new Random().NextDouble() * (10 + 10) - 10, 2); // [-10, 10]  элементы с дробью
}

double ArrayMin(double[] array)
{
    double minValue = array[0];
    for (int i = 1; i < array.Length; i++)
    {
        if (array[i] < minValue)
            minValue = array[i];
    }
    return minValue;
}

double ArrayMax(double[] array)
{
    double maxValue = array[0];
    for (int i = 1; i < array.Length; i++)
    {
        if (array[i] > maxValue)
            maxValue = array[i];
    }
    return maxValue;
}

Console.Clear();
Console.Write("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
double[] array = new double[n];
InputArray(array);
Console.WriteLine($"[{string.Join(", ", array)}]");
Console.WriteLine($"Результат: {ArrayMax(array) - ArrayMin(array)}");