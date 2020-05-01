package HeadFirstJava.Chapter4;

class Dog2 {

    int size;
    String name;

    void bark() {
        if (size > 60) {
        System.out.println("Wooof! Wooof");
        } else if (size > 14) {
        System.out.println("Ruff! Ruff!");
        } else {
            System.out.println("Yip! Yip!");
        }
    }

    void barks (int numOfBarks) {

        while (numOfBarks > 0) {

            if (size > 60) {
                System.out.println("Wooof!");
                } else if (size > 14) {
                System.out.println("Ruff!");
                } else {
                    System.out.println("Yip!");
                }

            numOfBarks = numOfBarks - 1;
        }
    }
}

class DogTestDrive {

    public static void main (String[] args) {
        Dog2 one = new Dog2();
        one.size = 70;
        Dog2 two = new Dog2();
        two.size = 8;
        Dog2 three = new Dog2();
        three.size = 35;

        one.barks(2);
        two.barks(7);
        three.barks(4);
    }
}