using System.ComponentModel.DataAnnotations.Schema;
using System.Security.Cryptography.X509Certificates;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System;

namespace _24.net
{
    class Program
    {
        static void Main(string[] args)
        {
            var components = File.ReadAllText("./input.txt").Split("\r\n")
                .Select(x => new Component
                {
                    L = Convert.ToInt32(x.Split('/')[0]),
                    R = Convert.ToInt32(x.Split('/')[1])
                })
                .ToList();

            // Part 1
            var max = components
                .Where(x => x.L == 0 || x.R == 0)
                .Select(x => GetStrongestBridge(x.R == 0 ? x.L : x.R, x, components.Where(y => y.R != x.R || y.L != x.L).ToList()))
                .Max();

            // Part 2
            var longest = components
                .Where(x => x.L == 0 || x.R == 0)
                .Select(x => GetLongestBridge(x.R == 0 ? x.L : x.R, x, components.Where(y => y.R != x.R || y.L != x.L).ToList()))
                .OrderByDescending(x => x.Item1)
                    .ThenByDescending(x => x.Item2)
                .First()
                .Item2;

            Console.WriteLine(longest);
        }

        static int GetStrongestBridge(int openPort, Component c, IList<Component> remainingComponents)
        {
            var maxNext = remainingComponents
                .Where(x => x.L == openPort || x.R == openPort)
                .Select(x => GetStrongestBridge(x.L == openPort ? x.R : x.L, x, remainingComponents.Where(y => y.R != x.R || y.L != x.L).ToList()))
                .ToList();

            if (maxNext.Count == 0)
                return c.L + c.R;
            else
                return c.L + c.R + maxNext.Max();
        }

        // (Depth, Strength)
        static (int, int) GetLongestBridge(int openPort, Component c, IList<Component> remainingComponents)
        {
            var maxNext = remainingComponents
                .Where(x => x.L == openPort || x.R == openPort)
                .Select(x => GetLongestBridge(x.L == openPort ? x.R : x.L, x, remainingComponents.Where(y => y.R != x.R || y.L != x.L).ToList()))
                .ToList();

            if (maxNext.Count == 0)
                return (1, c.L + c.R);
            else
            {
                var longestFromHere = maxNext.OrderByDescending(x => x.Item1).ThenByDescending(x => x.Item2).First();

                return (1 + longestFromHere.Item1, c.L + c.R + longestFromHere.Item2);
            }
        }

        public class Component
        {
            public int L;
            public int R;
            public override string ToString()
            {
                return $"L: {L}, R: {R}";
            }
        }
    }
}