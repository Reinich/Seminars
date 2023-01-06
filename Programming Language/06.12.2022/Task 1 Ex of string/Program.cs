Console.Clear();
string? n = Console.ReadLine(); // null-значение
Console.WriteLine(Convert.ToInt32(n?[0].ToString()) * 5); // char != string
