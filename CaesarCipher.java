import java.util.Scanner;

public class CaesarCipher {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input
        System.out.print("Enter text to encrypt: ");
        String text = scanner.nextLine();
        
        System.out.print("Enter shift value (e.g., 3): ");
        int shift = scanner.nextInt();

        // Encrypt
        String encrypted = encrypt(text, shift);
        System.out.println("\nCipher Text: " + encrypted);

        // Decrypt
        String decrypted = decrypt(encrypted, shift);
        System.out.println("Original Text: " + decrypted);
        
        scanner.close();
    }

    public static String encrypt(String text, int shift) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            char ch = text.charAt(i);

            if (Character.isUpperCase(ch)) {
                // 'A' is 65 in ASCII. We normalize to 0-25, shift, then convert back.
                char c = (char) (((ch - 'A' + shift) % 26) + 'A');
                result.append(c);
            } else if (Character.isLowerCase(ch)) {
                // 'a' is 97 in ASCII.
                char c = (char) (((ch - 'a' + shift) % 26) + 'a');
                result.append(c);
            } else {
                // Keep non-alphabetic characters (spaces, numbers) unchanged
                result.append(ch);
            }
        }
        return result.toString();
    }

    public static String decrypt(String text, int shift) {
        // Decryption is just encryption with a negative shift
        // We add 26 to ensure the result is positive before modulo
        return encrypt(text, 26 - (shift % 26));
    }
}
