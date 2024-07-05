import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Problem9465 {
    public class Main {

        public static void main(String[] args) throws IOException {
            BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

            int T = Integer.parseInt(bufferedReader.readLine());

            Solution solution = new Solution();

            for (int t = 0; t < T; t++) {
                solution.solution(Integer.parseInt(bufferedReader.readLine()));
            }
        }

        static class Solution {
            public void solution(int n) throws IOException {
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
                if (n == 1) {
                    System.out.println(Math.max(Integer.parseInt(bufferedReader.readLine()), Integer.parseInt(bufferedReader.readLine())));
                    return;
                }

                int[][] stickers = new int[2][n];
                int[][] DP = new int[2][n];

                for (int line = 0; line < 2; line++) {
                    String[] inputs = bufferedReader.readLine().split(" ");
                    for (int num = 0; num < n; num++) {
                        stickers[line][num] = Integer.parseInt(inputs[num]);
                    }
                }

                DP[0][0] = stickers[0][0];
                DP[1][0] = stickers[1][0];

                for (int i = 2; i < n; i++) {
                    DP[0][i] = Math.max(DP[1][i - 1], DP[1][i - 2]) + stickers[0][i];
                    DP[1][i] = Math.max(DP[0][i - 1], DP[0][i - 2]) + stickers[1][i];
                }

                System.out.println(Math.max(DP[0][n - 1], DP[1][n - 1]));
            }
        }
    }
}
