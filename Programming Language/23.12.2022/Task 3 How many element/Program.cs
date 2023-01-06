// Составить частотный словарь элементов двумерного массива. Частотный словарь содержит информацию о том, 
// сколько раз встречается элемент входных данных.

void OutputMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            Console.Write($"{matrix[i, j]} \t");
        Console.WriteLine();
    }
}

void InputMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
            matrix[i, j] = new Random().Next(-10, 11);
    }
    OutputMatrix(matrix);
}

void DictionaryMatrix(int[,] matrix)
{
    int count = 1;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            count = 1;
            if (matrix[i, j] != -100)
            {
                for (int k = 0; k < matrix.GetLength(0); k++)
                {
                    for (int m = 0; m < matrix.GetLength(1); m++)
                    {  
                        if (matrix[i, j] == matrix[k, m] && (i != k || j != m))
                        {
                            matrix[k, m] = -100;
                            count++;
                        }
                        // PrintMatrix(matrix);
                        // Console.WriteLine();
                    }
                }
                Console.WriteLine($"{matrix[i, j]} встречается {count} раз");
            }
        }
    }
}

Console.Clear();
Console.Write("Введите размеры матрицы: ");
int[] size = Console.ReadLine().Split(" ").Select(x => int.Parse(x)).ToArray();
int[,] matrix = new int[size[0], size[1]];
InputMatrix(matrix);

DictionaryMatrix(matrix);
Console.WriteLine();

OutputMatrix(matrix);








