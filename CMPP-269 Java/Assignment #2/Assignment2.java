/*
@Author Matthew Girado
November 1, 2020
Program is a mortgage calculator.
Program takes user input and stores the inputs in variables.
Program takes inputs and calculates user-dependant variables to create/print a table with costs outlined.
The program uses material learned from chapter 1 through 5 in CMPP-269's textbook.
 */
import java.util.*;
public class Assignment2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in); //Declares Scanner variable
        boolean validNumber = false; //Declares boolean validators
        boolean validTerm = false;
        boolean validPeriod = false;
        while (!validNumber) { //While loop that will error check and keep asking user for inputs until a valid one is entered, prints data and tables.
            System.out.print("Enter account number: ");
            String accountNumber = in.next();
            //Declares various variables for use in calculations later
            int sum;
            int doubleDigit2;
            int doubleDigit4;
            int doubleDigit6;
            double principalAmount;
            int mortgageTerm;
            int amortizationPeriod;

            /* If statement checks if the account number is the correct length
            If it is not the correct length it will ask user for account number again and tell them it is wrong
            Also has a for loop that checks the account number for letters, if one is found it will ask user
            for account number again and tell them what is wrong.
             */
            if (accountNumber.length() == 8) {
                for (int i = 0; i < 8; i++) {
                    char ch = accountNumber.charAt(i);
                    if (Character.isLetter(ch)) {
                        System.out.println("Invalid account number, letter found, digits only!");
                        break;
                    } else {
                        char digit1 = accountNumber.charAt(0); //This section of code converts user input into variables used later for check digit validation
                        char digit2 = accountNumber.charAt(1);
                        char digit3 = accountNumber.charAt(2);
                        char digit4 = accountNumber.charAt(3);
                        char digit5 = accountNumber.charAt(4);
                        char digit6 = accountNumber.charAt(5);
                        char digit7 = accountNumber.charAt(6);
                        char digit8 = accountNumber.charAt(7);
                        int digitOne = Integer.parseInt(String.valueOf(digit1));
                        int digitTwo = Integer.parseInt(String.valueOf(digit2));
                        int digitThree = Integer.parseInt(String.valueOf(digit3));
                        int digitFour = Integer.parseInt(String.valueOf(digit4));
                        int digitFive = Integer.parseInt(String.valueOf(digit5));
                        int digitSix = Integer.parseInt(String.valueOf(digit6));
                        int digitSeven = Integer.parseInt(String.valueOf(digit7));
                        int digitEight = Integer.parseInt(String.valueOf(digit8));
                        doubleDigit2 = digitTwo * 2; //Doubles every other digit in the account number.
                        doubleDigit4 = digitFour * 2;
                        doubleDigit6 = digitSix * 2;
                        //Account number is checked with the check digit to see if it is valid.
                        sum = digitOne + doubleDigit2 + digitThree + doubleDigit4 + digitFive + doubleDigit6 + digitSeven;
                        sum = sum % 10;
                        /* This section of code checks if the check digit is valid and asks the user to input account number again if it is invalid.
                        If check digits checks out, the code then continues with asking the user for various user input for data used in the table
                        and print statements later on.
                         */
                        if (sum != digitEight) {
                            System.out.println("Invalid account number, check digit does not match last digit!");
                            break;
                        } else {
                            System.out.print("Enter Client Name: ");
                            in.nextLine();
                            String clientName;
                            clientName = in.nextLine();
                            System.out.print("Enter Address of Mortgage property: ");
                            String mortgageProperty = in.nextLine();
                            System.out.print("Enter principal Amount: ");
                            principalAmount = in.nextDouble();
                            System.out.println("Available Terms and Rates");
                            System.out.printf("%10s%10s%n", "Term", "Rate");
                            System.out.printf("%10s%10s%n", "1 Year", "3.59%");
                            System.out.printf("%10s%10s%n", "2 Year", "3.74%");
                            System.out.printf("%10s%10s%n", "3 Year", "2.96%");
                            System.out.printf("%10s%10s%n", "5 Year", "3.29%");
                            System.out.printf("%10s%10s%n", "10 Year", "6.10%");
                            System.out.println("");
                            /* This section is the bulk of the code, checks if the user inputted valid mortgage term and
                            amortization periods. If incorrect, it loops back around and asks the user for a valid input.
                            If correct, it continues to print out various information for the user and then proceeds to print a
                            payment schedule table then terminates the program. This information applies all the way down
                            till the end.
                             */
                            while (!validTerm) {
                                System.out.print("Enter mortgage term in years (1, 2, 3, 5, 10): ");
                                mortgageTerm = in.nextInt();
                                if (mortgageTerm == 1) {
                                    while (!validPeriod) {
                                        System.out.print("Enter mortgage amortization period (5, 10, 15, 20, 25): ");
                                        amortizationPeriod = in.nextInt();
                                        double emr = 0.00296953385;
                                        double monthlyPayment = principalAmount * (emr * (Math.pow(1 + emr, 12 * amortizationPeriod)) / (Math.pow(1 + emr, 12 * amortizationPeriod) - 1));
                                        if (amortizationPeriod != 5 && amortizationPeriod != 10 && amortizationPeriod != 15 && amortizationPeriod != 20 && amortizationPeriod != 25) {
                                            System.out.println(amortizationPeriod + " is an invalid amortization period");
                                        } else {
                                            System.out.printf("%s%.2f%n", "Monthly payment amount is: ", monthlyPayment);
                                            System.out.println("");
                                            System.out.println("Payment schedule for " + clientName);
                                            System.out.println("Produced Wed Apr 29 17:08:10 MDT 2020");
                                            System.out.println("Property address: " + mortgageProperty);
                                            System.out.println("Amortization Period (in years): " + amortizationPeriod);
                                            System.out.println("Term of Mortgage (in years): " + mortgageTerm);
                                            System.out.println("Interest Rate: 3.59%");

                                            System.out.printf("%75s%n", "Monthly Payment Schedule");
                                            System.out.println("");
                                            System.out.printf("%s%20s%20s%20s%20s%20s%n", "Month", "Open Bal", "Payment", "Princ", "Interest", "Closing Bal");
                                            int x;
                                            double openingBalance = principalAmount;
                                            double totalPrinc = 0;
                                            double totalInterest = 0;
                                            for (x = 1; x <= 12; x++) {
                                                double monthlyInterest = openingBalance * emr;
                                                double monthlyPrinciple = monthlyPayment - monthlyInterest;
                                                double closingBalance = openingBalance - monthlyPrinciple;
                                                System.out.printf("%5d%20.2f%20.2f%20.2f%20.2f%20.2f%n", x, openingBalance, monthlyPayment, monthlyPrinciple, monthlyInterest, closingBalance);
                                                openingBalance -= monthlyPrinciple;
                                                totalInterest += monthlyInterest;
                                                totalPrinc += monthlyPrinciple;
                                            }
                                            int d;
                                            for (d = 0; d < 105; d++) {
                                                System.out.print('=');
                                            }
                                            System.out.println("");
                                            System.out.printf("%5s%60.2f%20.2f", "Ttls", totalPrinc, totalInterest);
                                            System.exit(0);
                                        }
                                    }
                                } else if (mortgageTerm == 2) {
                                    while (!validPeriod) {
                                        System.out.print("Enter mortgage amortization period (5, 10, 15, 20, 25): ");
                                        amortizationPeriod = in.nextInt();
                                        double emr = 0.00309265652;
                                        double monthlyPayment = principalAmount * (emr * (Math.pow(1 + emr, 12 * amortizationPeriod)) / (Math.pow(1 + emr, 12 * amortizationPeriod) - 1));
                                        if (amortizationPeriod != 5 && amortizationPeriod != 10 && amortizationPeriod != 15 && amortizationPeriod != 20 && amortizationPeriod != 25) {
                                            System.out.println(amortizationPeriod + " is an invalid amortization period");
                                        } else {
                                            System.out.printf("%s%.2f%n", "Monthly payment amount is: ", monthlyPayment);
                                            System.out.println("");
                                            System.out.println("Payment schedule for " + clientName);
                                            System.out.println("Produced Wed Apr 29 17:08:10 MDT 2020");
                                            System.out.println("Property address: " + mortgageProperty);
                                            System.out.println("Amortization Period (in years): " + amortizationPeriod);
                                            System.out.println("Term of Mortgage (in years): " + mortgageTerm);
                                            System.out.println("Interest Rate: 3.74%");

                                            System.out.printf("%75s%n", "Monthly Payment Schedule");
                                            System.out.println("");
                                            System.out.printf("%s%20s%20s%20s%20s%20s%n", "Month", "Open Bal", "Payment", "Princ", "Interest", "Closing Bal");
                                            int x;
                                            double openingBalance = principalAmount;
                                            double totalPrinc = 0;
                                            double totalInterest = 0;
                                            for (x = 1; x <= 12; x++) {
                                                double monthlyInterest = openingBalance * emr;
                                                double monthlyPrinciple = monthlyPayment - monthlyInterest;
                                                double closingBalance = openingBalance - monthlyPrinciple;
                                                System.out.printf("%5d%20.2f%20.2f%20.2f%20.2f%20.2f%n", x, openingBalance, monthlyPayment, monthlyPrinciple, monthlyInterest, closingBalance);
                                                openingBalance -= monthlyPrinciple;
                                                totalInterest += monthlyInterest;
                                                totalPrinc += monthlyPrinciple;
                                            }
                                            int d;
                                            for (d = 0; d < 105; d++) {
                                                System.out.print('=');
                                            }
                                            System.out.println("");
                                            System.out.printf("%5s%60.2f%20.2f", "Ttls", totalPrinc, totalInterest);
                                            System.exit(0);
                                        }
                                    }
                                } else if (mortgageTerm == 3) {
                                    while (!validPeriod) {
                                        System.out.print("Enter mortgage amortization period (5, 10, 15, 20, 25): ");
                                        amortizationPeriod = in.nextInt();
                                        double emr = 0.0024515917;
                                        double monthlyPayment = principalAmount * (emr * (Math.pow(1 + emr, 12 * amortizationPeriod)) / (Math.pow(1 + emr, 12 * amortizationPeriod) - 1));
                                        if (amortizationPeriod != 5 && amortizationPeriod != 10 && amortizationPeriod != 15 && amortizationPeriod != 20 && amortizationPeriod != 25) {
                                            System.out.println(amortizationPeriod + " is an invalid amortization period");
                                        } else {
                                            System.out.printf("%s%.2f%n", "Monthly payment amount is: ", monthlyPayment);
                                            System.out.println("");
                                            System.out.println("Payment schedule for " + clientName);
                                            System.out.println("Produced Wed Apr 29 17:08:10 MDT 2020");
                                            System.out.println("Property address: " + mortgageProperty);
                                            System.out.println("Amortization Period (in years): " + amortizationPeriod);
                                            System.out.println("Term of Mortgage (in years): " + mortgageTerm);
                                            System.out.println("Interest Rate: 2.96%");

                                            System.out.printf("%75s%n", "Monthly Payment Schedule");
                                            System.out.println("");
                                            System.out.printf("%s%20s%20s%20s%20s%20s%n", "Month", "Open Bal", "Payment", "Princ", "Interest", "Closing Bal");
                                            int x;
                                            double openingBalance = principalAmount;
                                            double totalPrinc = 0;
                                            double totalInterest = 0;
                                            for (x = 1; x <= 12; x++) {
                                                double monthlyInterest = openingBalance * emr;
                                                double monthlyPrinciple = monthlyPayment - monthlyInterest;
                                                double closingBalance = openingBalance - monthlyPrinciple;
                                                System.out.printf("%5d%20.2f%20.2f%20.2f%20.2f%20.2f%n", x, openingBalance, monthlyPayment, monthlyPrinciple, monthlyInterest, closingBalance);
                                                openingBalance -= monthlyPrinciple;
                                                totalInterest += monthlyInterest;
                                                totalPrinc += monthlyPrinciple;
                                            }
                                            int d;
                                            for (d = 0; d < 105; d++) {
                                                System.out.print('=');
                                            }
                                            System.out.println("");
                                            System.out.printf("%5s%60.2f%20.2f", "Ttls", totalPrinc, totalInterest);
                                            System.exit(0);
                                        }
                                    }
                                } else if (mortgageTerm == 5) {
                                    while (!validPeriod) {
                                        System.out.print("Enter mortgage amortization period (5, 10, 15, 20, 25): ");
                                        amortizationPeriod = in.nextInt();
                                        double emr = 0.00272306156;
                                        double monthlyPayment = principalAmount * (emr * (Math.pow(1 + emr, 12 * amortizationPeriod)) / (Math.pow(1 + emr, 12 * amortizationPeriod) - 1));
                                        if (amortizationPeriod != 5 && amortizationPeriod != 10 && amortizationPeriod != 15 && amortizationPeriod != 20 && amortizationPeriod != 25) {
                                            System.out.println(amortizationPeriod + " is an invalid amortization period");
                                        } else {
                                            System.out.printf("%s%.2f%n", "Monthly payment amount is: ", monthlyPayment);
                                            System.out.println("");
                                            System.out.println("Payment schedule for " + clientName);
                                            System.out.println("Produced Wed Apr 29 17:08:10 MDT 2020");
                                            System.out.println("Property address: " + mortgageProperty);
                                            System.out.println("Amortization Period (in years): " + amortizationPeriod);
                                            System.out.println("Term of Mortgage (in years): " + mortgageTerm);
                                            System.out.println("Interest Rate: 3.29%");

                                            System.out.printf("%75s%n", "Monthly Payment Schedule");
                                            System.out.println("");
                                            System.out.printf("%s%20s%20s%20s%20s%20s%n", "Month", "Open Bal", "Payment", "Princ", "Interest", "Closing Bal");
                                            int x;
                                            double openingBalance = principalAmount;
                                            double totalPrinc = 0;
                                            double totalInterest = 0;
                                            for (x = 1; x <= 12; x++) {
                                                double monthlyInterest = openingBalance * emr;
                                                double monthlyPrinciple = monthlyPayment - monthlyInterest;
                                                double closingBalance = openingBalance - monthlyPrinciple;
                                                System.out.printf("%5d%20.2f%20.2f%20.2f%20.2f%20.2f%n", x, openingBalance, monthlyPayment, monthlyPrinciple, monthlyInterest, closingBalance);
                                                openingBalance -= monthlyPrinciple;
                                                totalInterest += monthlyInterest;
                                                totalPrinc += monthlyPrinciple;
                                            }
                                            int d;
                                            for (d = 0; d < 105; d++) {
                                                System.out.print('=');
                                            }
                                            System.out.println("");
                                            System.out.printf("%5s%60.2f%20.2f", "Ttls", totalPrinc, totalInterest);
                                            System.exit(0);
                                        }
                                    }
                                } else if (mortgageTerm == 10) {
                                    while (!validPeriod) {
                                        System.out.print("Enter mortgage amortization period (5, 10, 15, 20, 25): ");
                                        amortizationPeriod = in.nextInt();
                                        double emr = 0.0050199113;
                                        double monthlyPayment = principalAmount * (emr * (Math.pow(1 + emr, 12 * amortizationPeriod)) / (Math.pow(1 + emr, 12 * amortizationPeriod) - 1));
                                        if (amortizationPeriod != 5 && amortizationPeriod != 10 && amortizationPeriod != 15 && amortizationPeriod != 20 && amortizationPeriod != 25) {
                                            System.out.println(amortizationPeriod + " is an invalid amortization period");
                                        } else {
                                            System.out.printf("%s%.2f%n", "Monthly payment amount is: ", monthlyPayment);
                                            System.out.println("");
                                            System.out.println("Payment schedule for " + clientName);
                                            System.out.println("Produced Wed Apr 29 17:08:10 MDT 2020");
                                            System.out.println("Property address: " + mortgageProperty);
                                            System.out.println("Amortization Period (in years): " + amortizationPeriod);
                                            System.out.println("Term of Mortgage (in years): " + mortgageTerm);
                                            System.out.println("Interest Rate: 6.10%");

                                            System.out.printf("%75s%n", "Monthly Payment Schedule");
                                            System.out.println("");
                                            System.out.printf("%s%20s%20s%20s%20s%20s%n", "Month", "Open Bal", "Payment", "Princ", "Interest", "Closing Bal");
                                            int x;
                                            double openingBalance = principalAmount;
                                            double totalPrinc = 0;
                                            double totalInterest = 0;
                                            for (x = 1; x <= 12; x++) {
                                                double monthlyInterest = openingBalance * emr;
                                                double monthlyPrinciple = monthlyPayment - monthlyInterest;
                                                double closingBalance = openingBalance - monthlyPrinciple;
                                                System.out.printf("%5d%20.2f%20.2f%20.2f%20.2f%20.2f%n", x, openingBalance, monthlyPayment, monthlyPrinciple, monthlyInterest, closingBalance);
                                                openingBalance -= monthlyPrinciple;
                                                totalInterest += monthlyInterest;
                                                totalPrinc += monthlyPrinciple;
                                            }
                                            int d;
                                            for (d = 0; d < 105; d++) {
                                                System.out.print('=');
                                            }
                                            System.out.println("");
                                            System.out.printf("%5s%60.2f%20.2f", "Ttls", totalPrinc, totalInterest);
                                            System.exit(0);
                                        }
                                    }
                                } else {
                                    System.out.println(mortgageTerm + " is an invalid term, please re-enter.");
                                }
                            }
                        }
                    }
                }
            } else {
                System.out.println("Invalid account number, the account number needs to be 8 digits");
                validNumber = false;
            }
        }
    }
}