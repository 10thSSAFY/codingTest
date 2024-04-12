StreamReader input = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
StreamWriter result = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));

string[] nums = input.ReadLine().Split();
int a = int.Parse(nums[0]);
int b = int.Parse(nums[1]);
int c = int.Parse(nums[2]);
int d = int.Parse(nums[3]);
int e = int.Parse(nums[4]);
int f = int.Parse(nums[5]);

int determinant = a * e - b * d;
int x = ((c * e) - (b * f)) / determinant;
int y = ((a * f) - (c * d)) / determinant;

result.Write($"{x} {y}");
result.Flush();

input.Close();
result.Close();