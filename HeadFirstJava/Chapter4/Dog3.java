package Chapter4;

public class Dog3 {
    int size;

    int getSize() {
        return size;
    }

    void setSize(int s) {
        size = s;
    }
}

class Dog3TestDrive {
    public static void main(String[] args) {
        Dog3[] pets;
        pets = new Dog3[7];

        pets[0] = new Dog3();
        pets[1] = new Dog3();

        pets[0].setSize(30);
        int x = pets[0].getSize();
        pets[1].setSize(8);
        int y = pets[1].getSize();
        System.out.println(x);
        System.out.println(y);
    }
}