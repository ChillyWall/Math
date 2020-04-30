package HeadFirstJava.Chapter1;

public class MyFirstApp {
    public static void main (String[] args) {
        int x = 4; // assign 4 to x

        while (x > 3) {
            //loop code will run because
            //x is greater than 3
            x = x - 1; // or we'd loop forever
        }
        int z = 27; //
        while (z == 17) {
            // loop code will not run because
            // z is not equal to 17
        }
    }

}
class IfTest {
    public static void main (String[] args) {
        int x = 3;
        if (x == 3) {
            System.out.println("x must be 3");
        }
        System.out.println("This runs no matter what");
    }
}

class IfTest2 {
    public static void main (String[] args) {
        int x = 2;
        if (x == 3) {
            System.out.println("x must be 3");
        } else {
            System.out.println("x is NOT 3");
        }
        System.out.println("This runs no matter what");
    }
}