// Sources Cited: Collier, R. "Lectures Notes for COMP1405B - Introduction to Computer Science I" [PDF document]. Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).
//Vineel Boddula 
//101018032 
import java.util.Scanner; //importing the scanner method to get userinput

public class a6q2 { 
	//Main function called automatically at the start of the class
	public static void main(String[] args)  {
		a6q2 MYINSTANCE = new a6q2(); //instances of the class
		
		try {	
			Scanner input = new Scanner(System.in); 
			System.out.print("Please enter an integer that you would like to find: ");

			int userInput = input.nextInt(); // get userinput
			
			int rowCounter = 0;   
			boolean sentinel = false;
			String stringValue = "";
			
			//do loop
			do {
				
				for (int i = 0; i < (rowCounter + 1); i++) {
				  
					int value = MYINSTANCE.combination(rowCounter, i); //using the combination function 
					stringValue = stringValue + String.valueOf(value) + " ";
					

					if (userInput == value) {
						sentinel = true;
					}

				}
				System.out.println(stringValue); // out the string value 
				rowCounter += 1; //counter
				stringValue = ""; // reset the variable 
			} while (sentinel == false); 
		} catch (Exception e){ //catch invalid input from the user 
			System.out.println("-----------------Invalid Input-----------------");
		}
    }
	
	//factorial method 
    public static int factorial(int x) {
        int factorialValue = x;
        int returnValue = 0;
		//return 1 if factorial value is less than 1 
        if (factorialValue <= 1) {
            returnValue = 1;
        } else {
            returnValue = 1;
            for (int i = 1; i <=factorialValue; i++) { 
                
                
                returnValue =returnValue * i;

            }
           
        }
        return returnValue;
    }

	//combination method 
    public static int combination(int n, int r) {
        int returnValue = ((factorial(n) / (factorial(r) * factorial(n - r)))); //using the factorial function
        
        if (returnValue == 0) {
            returnValue = 1;
        }
        
        return returnValue;
    }

}
