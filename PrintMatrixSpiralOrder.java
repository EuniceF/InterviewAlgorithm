public class PrintMatrixSpiralOrder {

    public static void spiralOrderPrint(int[][] matrix) {
        int tr = 0;
        int tc = 0;
        int dr = matrix.length - 1;
        int dc = matrix[0].length - 1;
        while (tr < dr) {
            printEdge(matrix, tr++, tc++, dr--, dc--);
        }
    }

    public static void printEdge(int[][] m, int tr, int tc, int dr, int dc) {
        if (tr == dr) {
            for (int i = tc; i <= dc; i++) {
                System.out.print(m[tr][i] + " ");
            }
        } else if (tc == dc) {
            for (int j = tr; j <= dr; j++) {
                System.out.println(m[j][tc]);
            }
        } else {
            int currC = tc;
            int currR = tr;
            while (currC != dc) {
                System.out.print(m[tr][currC] + " ");
                currC++;
            }
            while (currR != dr) {
                System.out.print(m[currR][dc] + " ");
                currR++;
            }
            while (currC != tc) {
                System.out.print(m[dr][currC] + " ");
                currC--;
            }
            while (currR != tr) {
                System.out.print(m[currR][tc] + " ");
                currR--;
            }
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
        spiralOrderPrint(matrix);
    }

}