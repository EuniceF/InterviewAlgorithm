public class ZigZagPrintMatrix {
    public static void printZigZagMatrix(int[][] matrix) {
        int tr = 0;
        int tc = 0;
        int dr = 0;
        int dc = 0;
        int endR = matrix.length - 1;
        int endC = matrix[0].length - 1;
        boolean fromUp = false;
        while (tr != endR + 1) {
            printLevel(matrix, fromUp, tr, tc, dr, dc);
            tr = tc == endC ? tr + 1 : tr;
            tc = tc == endC ? tc : tc + 1;
            dc = dr == endR ? dc + 1 : dc;
            dr = dr == endR ? dr : dr + 1;
            fromUp = !fromUp;
        }
        System.out.println();
    }

    public static void printLevel(int[][] m, boolean direction, int tr, int tc, int dr, int dc) {
        if (direction) {
            while (tr != dr + 1) {
                System.out.print(m[tr++][tc--] + " ");
            }
        } else {
            while (dr != tr - 1) {
                System.out.print(m[dr--][dc++] + " ");
            }
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
        printZigZagMatrix(matrix);
    }
}