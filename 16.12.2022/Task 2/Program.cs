Console.Clear();
Console.Write("Введите длину сторон: ");
int a = Convert.ToInt32(Console.ReadLine());
int b = Convert.ToInt32(Console.ReadLine());
int c = Convert.ToInt32(Console.ReadLine());
if ((c < a + b) && (b < a + c) && (a < b + c)) Console.WriteLine("Такой треугольник существует");
else Console.WriteLine("Такого быть не может");