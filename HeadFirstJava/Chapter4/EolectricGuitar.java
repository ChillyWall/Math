public class EolectricGuitar {
    
    private String brand;
    private int numOfPickups;
    private boolean rockStarUsesIt;

    String getBrand() {
        return brand;
    }

    void setBrand(String aBrand) {
        brand = aBrand;
    }

    int getNumOfPickups() {
        return numOfPickups; 
    }

    void setNumOfPickups(int num) {
        numOfPickups = num;
    }

    boolean getRockStarUsesIt() {
        return rockStarUsesIt;
    }

    void setRockStarUsesIt(boolean yesOrNo) {
        rockStarUsesIt = yesOrNo;
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
        System.out.pritnln(one.getRockStarUsesIt());
    }
}