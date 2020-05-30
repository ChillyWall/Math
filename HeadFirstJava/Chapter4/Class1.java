package Chapter4;

public class Class1 {
    public static void main(String[] args) {
        Class1 one = new Class1();
        int theSecret = one.giveSecret();
        System.out.println(theSecret);
    }

    int giveSecret() {
        return 42;
    }
}