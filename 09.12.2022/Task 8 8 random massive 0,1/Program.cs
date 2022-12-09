Console.Clear();
int[] n = new int[8];
for (int i = 0; i<n.Length; i++)
{
    n[i] = new Random().Next(0,2);
}
Console.WriteLine($"[{string.Join(", ", n)}]");
