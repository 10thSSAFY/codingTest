using System;
using System.IO;

public class Program
{
    private static readonly StreamReader reader = new StreamReader(Console.OpenStandardInput());
    private static readonly StreamWriter writer = new StreamWriter(Console.OpenStandardOutput());

    private static int index = 4;
    private static int[] arr = new int[11];

    public static void Main(string[] args)
    {
        int size = int.Parse(reader.ReadLine());

        arr[1] = 1;
        arr[2] = 2;
        arr[3] = 4;
        for (int i = 0; i < size; i++)
        {
            int num = int.Parse(reader.ReadLine());
            int result = GetResult(num);
            PrintResult(result);
        }

        reader.Close();
        writer.Close();
    }

    private static int GetResult(int num)
    {
        while (index <= num)
        {
            arr[index] = arr[index - 1] + arr[index - 2] + arr[index - 3];
            index++;
        }

        return arr[num];
    }

    private static void PrintResult(int result)
    {
        writer.WriteLine(result);
    }
}
