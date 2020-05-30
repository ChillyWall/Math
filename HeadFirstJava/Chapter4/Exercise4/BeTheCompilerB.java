package Chapter4.Exercise4;

class Clock {
    String time;

    void setTime(String t) {
        time = t;
    }

    String getTime() {
        return time;
    }
}

class ClockTestDrive {

    public static void main(String[] args) {

        Clock c1 = new Clock();
        c1.setTime("1245");
        String tod1 = c1.getTime();
        System.out.println("time: " + tod1);

        Clock c2 = new Clock();
        c2.setTime("1345");
        String tod2 = c2.getTime();
        System.out.println("time" + tod2);
    }
}