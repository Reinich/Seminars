//List - может хранить разные виды данных, 
Console.Clear();
Console.Write("Введите количество элементов: ");
int n  = Convert.ToInt32(Console.ReadLine());
int[] array = new int[n];
for (int i = 0; i <array.Length; i++)
{
    array[i] = new Random().Next(1, 11); // [1 , 10]
}
Console.WriteLine($"[{string.Join(", ", array)}]"); // Джоин позволяет соединить строку, обратный сплит, [] - для красоты

