import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        StringTokenizer st = new StringTokenizer(s);

        int[] arr = new int[6];
        for (int i=0 ; i<arr.length ; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.print( 1 - arr[0] + " ");
        System.out.print( 1 - arr[1] + " ");
        System.out.print( 2 - arr[2] + " ");
        System.out.print( 2 - arr[3] + " ");
        System.out.print( 2 - arr[4] + " ");
        System.out.print( 8 - arr[5] + " ");

    }

}