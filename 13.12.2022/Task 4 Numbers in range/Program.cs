void InputArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
        array[i] = new Random().Next(-100, 100);
}

int Find(int[] array)
{
    int count = 0;
    for (int i = 0; i < array.Length; i++)
    {
        if (array[i] > 10 && array[i] < 100) count++;
    }
    return count;
}

Console.Clear();
int[] array = new int[123];
InputArray(array);
Console.WriteLine(Find(array));
