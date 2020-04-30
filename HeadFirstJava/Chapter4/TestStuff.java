package HeadFirstJava.Chapter4;

public class TestStuff {
    public static void main (String[] args) {
        TestStuff t = new TestStuff();
        int foo = 7;
        int bar = 3;
        t.takeTwo(foo, bar);
    }

    void takeTwo(int x, int y) {
        int z = x + y;
        System.out.println("Total is " + z);
    }
}