void InputArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        array[i] = new Random().Next(-5, 10);
}

string ReleaseArray(int[] array, int k) // То, что возвращает, тот тип и указываем
{
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] == k)
            return "Это число есть в массиве";
    }
    return "Этого числа нет в массива";
}

Console.Clear();
Console.Write("Введите кол-во элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
InputArray(array);
Console.WriteLine($"Начальный массив: [{string.Join(", ", array)}]");
Console.Write("Введите число: ");
int k = Convert.ToInt32(Console.ReadLine());
Console.WriteLine(ReleaseArray(array, k));


