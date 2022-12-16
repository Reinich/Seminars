void InputArray(int[] array)
{
    for (int i = 0; i < (array.Length / 2); i++)
        array[i] = new Random().Next(1, 11);
}
void ReleaseArray(int[] array)
{
    for (int i = 0; i < (array.Length / 2); i++)
    {
        int temp = array[i];
        array[i] = array[array.Length - i - 1];
        array[array.Length - i - 1] = temp;
    }
}

Console.Clear();
Console.Write("Введите количество элементов: ");
// int[] s = Console.ReadLine().Split(" ").Select(x => int.Parse(x)).ToArray();
// foreach (int element in s)
//     Console.WriteLine(element * 2);
int n = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
InputArray(array);
Console.WriteLine($"[{string.Join(", ", array)}]");
ReleaseArray(array);
Console.WriteLine($"[{string.Join(", ", array)}]");

