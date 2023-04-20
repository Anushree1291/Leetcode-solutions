class Solution {
    // private static int[] sequence = new int[30];
    // private static int[] sequence = new int[] {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040};

    public int fib(int n) {
        return (int) Math.round((Math.pow(1.618033988749895, n) - Math.pow(-0.618033988749895, n)) / 2.23606797749979);
        // return sequence[n];
        // sequence[0] = 1;
        // sequence[1] = 1;

        // System.out.print("{1, 1");

        // for (int i = 2; i < 30; ++i) {
        //     sequence[i] = sequence[i-2] + sequence[i-1];
        //     System.out.print(", " + sequence[i]);
        // }

        // System.out.println("}");

        // return sequence[n-1];
    }
}