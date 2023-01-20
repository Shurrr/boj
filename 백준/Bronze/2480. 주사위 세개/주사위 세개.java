import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.Buffer;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        int result;
        int firstDice = Integer.parseInt(st.nextToken());
        int secondDice = Integer.parseInt(st.nextToken());
        int thirdDice = Integer.parseInt(st.nextToken());

        if (firstDice == secondDice && secondDice == thirdDice ) {
            result = 10000 + firstDice * 1000;
        }
        else if (firstDice == secondDice ) {
            result = 1000 + firstDice * 100;
        }

        else if (firstDice == thirdDice) {
            result = 1000 + firstDice * 100;
        }

        else if (secondDice == thirdDice) {
            result = 1000 + secondDice * 100;
        }

        else {
            result = Math.max(firstDice,  Math.max(secondDice, thirdDice)) * 100;
        }

        System.out.println(result);

    }

}