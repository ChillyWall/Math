package Chapter5;

import java.io.*;

/* prepcode
DECLARE an int array to hold the location cells. Call it locationCells.
DECLARE an int to hold the number of hits. Call it numOfHits and SET it to 0.

DECLARE a checkYourself() method that takes a String for the user’s guess (“1”, “3”, etc.), checks it, and returns a result representing a “hit”, “miss”, or “kill”.
DECLARE a setLocationCells() setter method that takes an int array (which has the three cell locations as ints (2, 3, 4, etc.).

METHOD: String checkYourself(String userGuess)
    GET the user guess as a String parameter
    CONVERT the user guess to an int
    REPEAT with each of the location cells in the int array
        // COMPARE the user guess to the location cell
        IF the user guess matches
            INCREMENT the number of hits
            // FIND OUT if it was the last location cell:
            IF number of hits is 3, RETURN “kill” as the result
            ELSE it was not a kill, so RETURN“hit”
            END IF
            ELSE the user guess did not match, so RETURN “miss”
        END IF
    END REPEAT
END METHOD

METHOD: void setLocationCells(int[] cellLocations)
    GET the cell locations as an int array parameter
    ASSIGN the cell locations parameter to the cell locations instance variable
END METHOD
 */

class SimpleDotComTestDrive {

    public static void main(String[] args) {
        SimpleDotCom dot = new SimpleDotCom();

        int[] location = { 2, 3, 4 };
        dot.setLocationCells(location);

        String userGuess = "2";
        String result = dot.checkYourselfIf(userGuess);
        String testResult = "failed";
        if (result.equals("hit")) {
            testResult = "passed";
        }
        System.out.println(testResult);
    }
}

class SimpleDotCom {

    int[] locationCells;
    int numOfHits;

    public void setLocationCells(int[] locs) {
        locationCells = locs;
    }

    public String checkYourselfIf(String stringGuess) {
        int guess = Integer.parseInt(stringGuess);
        String result = "miss";

        for (int cell : locationCells) {
            if (guess == cell) {
                result = "hit";
                numOfHits++;
                break;
            }
        } // out of loop

        if (numOfHits == locationCells.length) {
            result = "kill";
        }
        System.out.println(result);
        return result;
    } // close method
} // close class

/*
 * Method public static void main (String[] args) DECLARE an int variable to
 * hold the number of Guesses called numOfGuess Make the single SimpleDotCom
 * Object COMPUTE an random number between 1 and 4 that will be the starting
 * location MAKE an int array with 3 ints using the randomly-generated number,
 * that number incremented by 1, and that number incremented by 2 (example:
 * 3,4,5) INVOKE the setLocationCells() method on the SimpleDotCom instance
 * DECLARE a boolean variable representing the stage of the game called isAlive,
 * SET it to true
 * 
 * WHILE the dot is alive now GET the input of user // CHECK the result INVOKE
 * checkYourselfIf() method in SimpleDotCom instance INCREMENT numOfGuesses IF
 * result == "kill" SET isAlive to false PRINT the numOfGuess
 */

class SimpleDotComGame {
    public static void main(String[] args) {
        int numOfGuesses = 0;
        GameHelper helper = new GameHelper();

        SimpleDotCom theDotCom = new SimpleDotCom();
        int randomNum = (int) (Math.random() * 5);

        int[] locations = { randomNum, randomNum + 1, randomNum + 2 };
        theDotCom.setLocationCells(locations);
        boolean isAlive = true;

        while (isAlive) {
            String guess = helper.getUserInput("enter a num");
            String result;
            if (guess == null) {
                continue;
            } else {
                result = theDotCom.checkYourselfIf(guess);
                numOfGuesses++;
            }

            if (result.equals("kill")) {
                isAlive = false;
                System.out.println("You took " + numOfGuesses + " guesses");
            } // close if
        } // close while
    } // close main
}

class GameHelper {
    public String getUserInput(String prompt) {
        String inputLine = null;
        System.out.print(prompt + " ");
        try {
            BufferedReader is = new BufferedReader(new InputStreamReader(System.in));
            inputLine = is.readLine();
            if (inputLine.length() == 0)
                return null;
        } catch (IOException e) {
            System.out.println("IOException: " + e);
        }
        return inputLine;
    }
}