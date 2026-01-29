import java.util.*;

public class PlayfairCipher {

  static char[][] keyMatrix = new char[5][5];

  static void generateKeyMatrix(String key) {
    boolean[] used = new boolean[26];
    key = key.toUpperCase().replace("J", "I").replaceAll("[^A-Z]", "");

    int k = 0;
    for (char c : key.toCharArray()) {
      if (!used[c - 'A']) {
        keyMatrix[k / 5][k % 5] = c;
        used[c - 'A'] = true;
        k++;
      }
    }

    for (char c = 'A'; c <= 'Z'; c++) {
      if (c == 'J')
        continue;
      if (!used[c - 'A']) {
        keyMatrix[k / 5][k % 5] = c;
        k++;
      }
    }
  }

  static int[] find(char c) {
    for (int i = 0; i < 5; i++)
      for (int j = 0; j < 5; j++)
        if (keyMatrix[i][j] == c)
          return new int[] { i, j };
    return null;
  }

  static String prepare(String text) {
    text = text.toUpperCase().replace("J", "I").replaceAll("[^A-Z]", "");
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < text.length(); i++) {
      sb.append(text.charAt(i));
      if (i + 1 < text.length() && text.charAt(i) == text.charAt(i + 1))
        sb.append('X');
    }

    if (sb.length() % 2 != 0)
      sb.append('X');

    return sb.toString();
  }

  static String encrypt(String text) {
    text = prepare(text);
    StringBuilder out = new StringBuilder();

    for (int i = 0; i < text.length(); i += 2) {
      int[] a = find(text.charAt(i));
      int[] b = find(text.charAt(i + 1));

      if (a[0] == b[0]) {
        out.append(keyMatrix[a[0]][(a[1] + 1) % 5]);
        out.append(keyMatrix[b[0]][(b[1] + 1) % 5]);
      } else if (a[1] == b[1]) {
        out.append(keyMatrix[(a[0] + 1) % 5][a[1]]);
        out.append(keyMatrix[(b[0] + 1) % 5][b[1]]);
      } else {
        out.append(keyMatrix[a[0]][b[1]]);
        out.append(keyMatrix[b[0]][a[1]]);
      }
    }
    return out.toString();
  }

  static String decrypt(String text) {
    StringBuilder out = new StringBuilder();

    for (int i = 0; i < text.length(); i += 2) {
      int[] a = find(text.charAt(i));
      int[] b = find(text.charAt(i + 1));

      if (a[0] == b[0]) {
        out.append(keyMatrix[a[0]][(a[1] + 4) % 5]);
        out.append(keyMatrix[b[0]][(b[1] + 4) % 5]);
      } else if (a[1] == b[1]) {
        out.append(keyMatrix[(a[0] + 4) % 5][a[1]]);
        out.append(keyMatrix[(b[0] + 4) % 5][b[1]]);
      } else {
        out.append(keyMatrix[a[0]][b[1]]);
        out.append(keyMatrix[b[0]][a[1]]);
      }
    }
    return out.toString();
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    System.out.print("Enter key: ");
    String key = sc.nextLine();
    generateKeyMatrix(key);

    System.out.print("Enter plaintext: ");
    String plain = sc.nextLine();

    String cipher = encrypt(plain);
    System.out.println("Encrypted: " + cipher);
    System.out.println("Decrypted: " + decrypt(cipher));
  }
}
