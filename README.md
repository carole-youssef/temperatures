# temperatures
Temperature analysis program

Overview:
- This Python program allows users to input midday and midnight temperatures for a span of three days. It then calculates and presents various temperature statistics, including total, average,
  highest midday temperature, and lowest midnight temperature.

Instructions for Use:
1) Input Midday and Midnight Temperatures:
- The program prompts the user to input midday and midnight temperatures for each of the three days.
- Temperatures must be between 0 and 100 degrees. If the input is out of range, the user will be prompted to re-enter the temperature.
2) View Results:
- The program displays the following results:
- Sum of midday temperatures.
- Sum of midnight temperatures.
- Average midday temperature.
- Average midnight temperature.
- Highest midday temperature and the day it occurred.
- Lowest midnight temperature and the day it occurred.

Code Structure:
- The program utilizes two lists (daytemp and nighttemp) to store midday and midnight temperatures, respectively.
- A function named Temperatures is defined to handle the input of temperatures for each day.
- A loop iterates three times to collect temperatures for three days.
- After collecting temperatures, the program calculates the sum and average of midday and midnight temperatures.
- It also identifies the highest midday temperature and the lowest midnight temperature along with the respective days.

Potential Enhancements:

User-Friendly Interface:
- Consider enhancing the user interface by providing clearer instructions and feedback.
  
Expandability:
- The program currently handles three days; however, it can be extended to handle a dynamic number of days by adjusting loop conditions.

Data Validation:
- Implement additional data validation checks to ensure input correctness and prevent potential errors.

How to Run:
- Ensure you have Python installed on your system.
- Copy and paste the code into a Python file (e.g., temperature_analysis.py).
- Run the script using a Python interpreter.
- Follow the on-screen prompts to input temperatures.
