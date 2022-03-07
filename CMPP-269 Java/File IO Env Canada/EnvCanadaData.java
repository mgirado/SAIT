/**
 * EnvCanadaData - Program to process an Environment Canada
 * data file and calculate the average maximum and minimum temperature
 *
 * @author Dave Leskiw
 * @version Feb 2020
 */
// Standard import for the Scanner class
import java.util.*;
import java.io.*;
public class Main
{
    public static void main (String [] args) throws IOException
    {
        // Create a Scanner object attached to the keyboard
        Scanner in = new Scanner (System.in);
        System.out.print ("Enter the filename: ");
        String filename = in.nextLine();
        File file = new File(filename);
        Scanner inFile = new Scanner(file).useDelimiter (",");

        // Read and discard header line
        inFile.nextLine();
        int numMinDays = 0;
        double totalMinTemps = 0;
        double minTemp;
        int year, month, day;
        // while more data
        while (inFile.hasNext())
        {
            // discard 5 columns
            for (int i = 0; i < 5;i++)
            {
                inFile.next();
            }
            // read year, month, day
            year = inFile.nextInt();
            month = inFile.nextInt();
            day = inFile.nextInt();
            // discard data qualifier
            inFile.next();
            inFile.next();
            inFile.next();
            // read max temp
            String tempS = inFile.next();
            // Check to see if a min temperature was present
            if (!tempS.equals(""))
            {
                // temperature present convert to double
                minTemp = Double.parseDouble (tempS);
                totalMinTemps += minTemp;
                numMinDays++;

            }
            // discard the rest of the line on the line
            inFile.nextLine();

        } // loop to process all temperatures
        inFile.close();
        double average = totalMinTemps/numMinDays;
        System.out.printf ("# of days Min Temperature reported = %d%n", numMinDays);
        System.out.printf ("The average minimum temperature is %.2f%n",
                average);
    }
}

