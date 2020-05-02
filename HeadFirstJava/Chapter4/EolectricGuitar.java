package Chapter4;

public class EolectricGuitar {

    private String brand;
    private int numOfPickups;
    private boolean rockStarUsesIt;

    void setBrand(String aBrand) {
        brand = aBrand;
    }

    String getBrand() {
        return brand;
    }

    void setNumOfPickups(int num) {
        numOfPickups = num;
    }

    int getNumOfPickups() {
        return numOfPickups; 
    }

    void setRockStarUsesIt(boolean yesOrNo) {
        rockStarUsesIt = yesOrNo;
    }

    boolean getRockStarUsesIt() {
        return rockStarUsesIt;
    }
}

class EolectricGuitarTestDrive {

    public static void main (String[] args) {
        EolectricGuitar one = new EolectricGuitar();
        one.setBrand("My Heart Will Go On");
        one.setNumOfPickups(3);
        one.setRockStarUsesIt(false);
        System.out.println(one.getBrand());
        System.out.println(one.getNumOfPickups());
        System.out.println(one.getRockStarUsesIt());
        EolectricGuitar two = new EolectricGuitar();
        two.setBrand("Dream it Possible");
        two.setNumOfPickups(2);
        two.setRockStarUsesIt(true);
        System.out.println(two.getBrand());
        System.out.println(two.getNumOfPickups());
        System.out.println(two.getRockStarUsesIt());
    }
}