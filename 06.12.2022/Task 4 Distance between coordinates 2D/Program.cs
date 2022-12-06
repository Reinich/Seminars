Console.Clear();

//double result = Math.Sqrt(25) - корень из числа; //Math.Pow() - степень, нужно два числа, первое - что нужно возвести, второе - степень;
Console.WriteLine("Введите первые координаты: ");
double x1 = Convert.ToInt32(Console.Read());
double y1 = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите вторые координаты: ");
double x2 = Convert.ToInt32(Console.Read());
double y2 = Convert.ToInt32(Console.ReadLine());

double l = Math.Sqrt(Math.Pow(x1 - x2, 2) + Math.Pow(y1 - y2, 2));
Console.WriteLine($"Расстояние = {Math.Round(l, 2)}");
