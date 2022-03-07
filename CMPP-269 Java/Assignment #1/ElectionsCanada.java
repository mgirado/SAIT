
/**
 * ElectionsCanada - I use the java utility scanner to read input from users multiple times.
 * I used it to get the user to enter data for candidate names.
 * I used it to get the user to enter data for electoral district name.
 * I used it to get the user to enter data for number of eligible voters.
 * I used it to get the user to enter data for polling station data.
 * I used printf, print, and println to print out text for the user to read, using different ones for different situations.
 * I used printf to properly format the table.
 * I did basic math, using "double" and the various java operators to get it do the math required.
 * @Matthew Girado
 * October 1, 2020
 */
// Standard import for the Scanner class
import java.util.*;
public class ElectionsCanada {
    public static void main(String[] args) {
       // Create a Scanner object attached to the keyboard
       Scanner input = new Scanner(System.in);
       // Write your code here!!!!
       
       System.out.print("Electoral district name: ");
       String electoralDistrict = input.nextLine();
       //Asks user to input electoral district name
         
       System.out.print("Number of eligible voters in Calgary Confederation: ");
       double eligibleVoters = input.nextDouble();
       //Asks user to input number of eligible voters
        
       System.out.print("CPC candidate name: ");
       String cpcCandidate = input.next();
       System.out.print("GPC candidate name: ");
       String gpcCandidate = input.next();
       System.out.print("LPC candidate name: ");
       String lpcCandidate = input.next();
       System.out.print("NDP candidate name: ");
       String ndpCandidate = input.next();
       System.out.print("PPC candidate name: ");
       String ppcCandidate = input.next();
       //Asks user to input candidate names
         
       System.out.println("Polling station 1 data (CPC# GPC# LPC# NDP# PPC#): ");
       double cpcVotersS1 = input.nextDouble();
       double gpcVotersS1 = input.nextDouble();
       double lpcVotersS1 = input.nextDouble();
       double ndpVotersS1 = input.nextDouble();
       double ppcVotersS1 = input.nextDouble();
       //Asks user to input polling station 1 data
       
       System.out.println("Polling station 2 data (CPC# GPC# LPC# NDP# PPC#): ");
       double cpcVotersS2 = input.nextDouble();
       double gpcVotersS2 = input.nextDouble();
       double lpcVotersS2 = input.nextDouble();
       double ndpVotersS2 = input.nextDouble();
       double ppcVotersS2 = input.nextDouble();
       //Asks user to input polling station 2 data
        
       double cpcTotal = cpcVotersS1 + cpcVotersS2;
       double gpcTotal = gpcVotersS1 + gpcVotersS2;
       double lpcTotal = lpcVotersS1 + lpcVotersS2;
       double ndpTotal = ndpVotersS1 + ndpVotersS2;
       double ppcTotal = ppcVotersS1 + ppcVotersS2;
       //Calculates each candidate's vote totals
        
       double allTotal = cpcTotal + gpcTotal + lpcTotal + ndpTotal + ppcTotal;
       //Calculates total voters
        
       double cpcPercent = cpcTotal / allTotal * 100;
       double gpcPercent = gpcTotal / allTotal * 100;
       double lpcPercent = lpcTotal / allTotal * 100;
       double ndpPercent = ndpTotal / allTotal * 100;
       double ppcPercent = ppcTotal / allTotal * 100;
       //Calculates party vote percentages
        
       double turnoutPercent = allTotal / eligibleVoters * 100;
       //Calculates turnout percentage
        
       System.out.println(""); //Add empty line
       System.out.println(""); //Add empty line
       System.out.println("Results for Calgary Confederation");
       System.out.println(""); //Add empty line
        
       System.out.printf("%10s%15s%10s%10s\n", "Party", "Candidate", "Votes", "% Vote");
       System.out.printf("%10s%15s%10.0f%10.1f\n", "CPC", cpcCandidate, cpcTotal, cpcPercent);
       System.out.printf("%10s%15s%10.0f%10.1f\n", "GPC", gpcCandidate, gpcTotal, gpcPercent);
       System.out.printf("%10s%15s%10.0f%10.1f\n", "LPC", lpcCandidate, lpcTotal, lpcPercent);
       System.out.printf("%10s%15s%10.0f%10.1f\n", "NDP", ndpCandidate, ndpTotal, ndpPercent);
       System.out.printf("%10s%15s%10.0f%10.1f\n", "PPC", ppcCandidate, ppcTotal, ppcPercent);
       System.out.printf("%10s%25.0f\n", "Total", allTotal);
       //Prints out entire table with votes, vote percentage, candidate names, and parties they belong to
       
       System.out.println(""); //Add empty line
       System.out.printf("Voter turnout %.0f/%.0f = %.1f%s\n", eligibleVoters, allTotal, turnoutPercent, "%");
       
        
    }
}
