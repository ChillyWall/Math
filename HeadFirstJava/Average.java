import org.jetbrains.annotations.NotNull;

import java.util.Arrays;

public class Average {
    int[] numbers;
    int[] weight;
    boolean ifCompleted;
    private int average;
    private int weightedAverage;
    private int [] publicNum;
    private int median;
    private int variance;

    void setData(int[] n, int[] w, boolean i ) {
        numbers = n;
        weight = w;
        ifCompleted = i;
    }

    void setAverage (int @NotNull [] numbers) {
        int numUsed = 0;
        for (int num : numbers) {
            numUsed += num;
        }
        average = numUsed / numbers.length;
    }

    int getAverage() {
        return average;
    }

    void setWeightedAverage(int @NotNull [] numbers, int[]weight) {
        int l = numbers.length;
        int total = 0;
        for (int i = 0; i < l; i++) {
            total += numbers[i] * weight[i];
        }
        weightedAverage = total / l;
    }

    int getWeightedAverage() {
        return weightedAverage;
    }
    void setPublicNum(int[] numbers) {

    }
}

class AverageTestDrive {
    public static void main(String[] args) {
        int[] numbers = {1, 2, 3, 4, 5, 6};
        int[] weight = {1, 2, 3, 4, 5, 6};
        boolean ifCompleted = false;
        Average one = new Average();
        one.setData(numbers, weight, ifCompleted);
        one.setWeightedAverage(numbers, weight);
        System.out.println(one.getWeightedAverage());
    }
}