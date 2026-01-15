import java.util.Scanner;

public class PasswordXOR {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input Password
        System.out.print("Enter Password: ");
        String password = scanner.nextLine();

        // Input Key (single char or integer for simplicity)
        System.out.print("Enter a secret Key (single character): ");
        char key = scanner.next().charAt(0);

        // Encrypt
        String encrypted = process(password, key);
        System.out.println("\nEncrypted Password: " + encrypted);

        // Decrypt
        String decrypted = process(encrypted, key);
        System.out.println("Decrypted Password: " + decrypted);
        
        scanner.close();
    }

    // Method to handle both Encryption and Decryption (Symmetric)
    public static String process(String input, char key) {
        char[] chars = input.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            // XOR operation
            chars[i] = (char) (chars[i] ^ key);
        }
        return new String(chars);
    }
}
