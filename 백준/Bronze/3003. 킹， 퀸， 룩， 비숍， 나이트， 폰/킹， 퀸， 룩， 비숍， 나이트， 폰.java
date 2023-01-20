import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        int[] chess = new int[] {1, 1, 2, 2, 2, 8};
        int[] foundChess = new int[6];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0 ; i < foundChess.length ; i++) {
            foundChess[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0 ; i < chess.length; i++) {
            System.out.print( chess[i] - foundChess[i] + " ");
        }
    }

}
