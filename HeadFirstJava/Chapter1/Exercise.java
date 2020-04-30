package HeadFirstJava.Chapter1;

class shuffle1 {
    public static void main (String[] args) {
        int x = 3;
        while (x > 0) {

            if (x > 2) {
                System.out.print("a");
            }

            x = x - 1;
            System.out.print("-");

            if (x == 2) {
                System.out.print("b c");
            }

            if (x == 1) {
                System.out.print("d");
                x = x - 1;
            }
        } //end the while loop
    } //end the main
} //end the class


class Exercise1bA {
    public static void main(String[] args) {
        int x = 1;
        while (x < 10) {
            x = x + 1;
            if (x > 3) {
                System.out.println("big x");
            }
        }
    }
}


class Exercise1bB {
    public static void main(String[] args) {
        int x = 5;
        while (x > 1) {
            x = x - 1;
            System.out.println("small x");
        }
    }
}


class Exercise1bC {
    public static void main(String[] args) {
        int x = 5;
        while (x > 1) {
            x = x - 1;
            System.out.println("small x");
        }
    }
}


class Exercise1c {
    public static void main(String[] args) {
        int x = 0;
        int y = 0;
        while (x < 5) {
            y = x - y;
            System.out.println(x + "" + y + " ");
            x = x + 1;
        }
    }
}


class PoolPuzzleOne {
    public static void main(String[] args) {
        int x = 0;
        while(x < 4) {
            System.out.print("a");
            if ( x < 1) {
                System.out.print(" ");
            }
            System.out.print("n");

            if (x > 1) {

                System.out.print(" oyster");
                x = x + 2;
            }
            if (x == 1) {

                System.out.print("noys");
            }
            if (x < 1) {

                System.out.print("oise");
            }
            System.out.println("");

            x = x + 1;
        }
    }
}
