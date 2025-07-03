'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Assignment 1 - Part A
#Assignment Revised/debugged

#Task 1
#Author: Jayden Nair
def FarenHeitToCelsius(Farenheit):
#Converts temperature in Farenheit to Celsius
#Takes in input in Farenheit and returns an output in celsius
 Farenheit = float(Farenheit)
 Celsius = (Farenheit - 32) * 5/9
 return Celsius



#Task 2
#Author: Jayden Nair
def NumRealRoots(a,b,c):
#Calculates the number of real roots in a quadratic
#Takes in 3 inputs corresponding to quadratic coefficients a,b and c
#Returns the number of real roots as an output
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 0 
    elif discriminant > 0: 
       return 2 
    else:
        return 1
        

#Task 3
#Author: Jayden Nair
def factorial(n):
#Calculates factorial of a positive integer
#Takes in a positive integer (n) and returns the factorial of n
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
    
#task 4
#Author: Jayden Nair
def ExpSeries(x,t):
#Uses Taylor Series expansion to approximate exponential function exp(x)
#Takes in a value x for exp(x) and a value t for the number of terms in the series
#the function will return the value of exp(x) with t terms
#An error prompt will be returned if t is not a positive integer
   x = float(x)
   if t <= 0 or t % 1 != 0:
       return "ExpSeries error: number of terms is not a positive integer"
   result = 0
   for n in range(t):
       result += (x**n) / factorial(n)
   return result
   
   
   #task 5
#Author: Jayden Nair
import math
def CartesianToPolar(x,y):
#Converts cartesian coordinates to polar coordinates
#takes in two inputs x,y corresponding to cartesian coordinates
#returns the corresponding polar coordinates (r, theta)
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y,x)
    return [r,theta]
    

#Assignment 1 - Part B
#task 6
#Author: Jayden Nair
def bin2dec(binary_input):
#Converts a binary string to it's corresponding decimal value
#takes in a binary input string and returns the decimal equivalent


      if type(binary_input) != str:
        return "Error: input must be a valid binary string"
      #an error prompt will be returned if the input is not a string
  
      if binary_input == "":
          return "Error: input must be a valid binary string"
 
      binary_input = binary_input.replace(" ", "")
      
      if not all(bit in "01" for bit in binary_input):
          return "Error: input must be a valid binary string"
          

      if binary_input.startswith("0b"):
          digit_binary = binary_input[2:]
      else:
          digit_binary = binary_input
          
      decimal = 0
      length = len(digit_binary)

      for i in range(length):
          bit_value = int(digit_binary[i])
          exponent = length - 1 - i
          decimal += (bit_value * (2**exponent))
      return decimal
      
#task 7
#Author: Jayden Nair
def hex2dec(hex_int):
#converts a hexidecimal string to it's corresponding decimal value
#takes in a hexidecimal string input and returns the decimal equivalent as an output
   if type(hex_int) != str:
       return "Error: input must be a string"
       #an error prompt will be returned if the input is not a string
       
   if hex_int == "":
       return "Error: input must be a string"
       
   if hex_int.startswith("0x"):
        digit_hex = hex_int[2:]
   else:
        digit_hex = hex_int
   #ensures the sliced hexadecimal string is all capitals to fit the if-else clause
   digit_hex = digit_hex.upper()

   decimal = 0 
   length = len(digit_hex)
    
   for i in range(length):
        
        if "0" <= digit_hex[i] <= "9":
            int_value = int(digit_hex[i])
        elif "A" <= digit_hex[i] <= "F":
            int_value = ord(digit_hex[i]) - ord("A") + 10
    
        else:
            return "Error: Invalid Hexadecimal Character"
        
        exponent = length - i - 1
        decimal  += int_value * (16 ** exponent)
    
   return decimal
   
   #task 8
#Author: Jayden Nair
def dec2bin(n):
#converts a decimal number to it's binary equivalent
#takes in an decimal integer as an input and returns
#the corresponding binary number as an output
    
    if type(n) != int:
        return "Error: Input must be an integer"
        #if the decimal value is not an integer display error message  
    elif n < 0:
        return "Error: negative numbers not handled"
        #if the decimal integer is negative display error message       
    if n == 0:
        return "0b0"
    m = "" 
    while n != 0:
        r =  n % 2   
        n = n//2
        m = str(r) + m
    return "0b" + m
    
    
    
#task 9
#Author: Jayden Nair
#concatinates a list containing unicode(s) points with a string 
#takes in a string and a list as an input and outputs a concatinated message
def appendCodePoints(string, code_points):
    for values in code_points:
        
        hex_val = values[2:]
        
        dec_val = hex2dec(hex_val)
        #convert the decimal number to the corresponding emoji using the chr function
        unicode_val = chr(dec_val)
        
        string += unicode_val
    return string
    
    
#task 10
#Author: Jayden Nair
#The function converts a 16-bit IEEE 754 half-precision floating-point binary string to 
#decimal float
def half2dec(IEEE_754):
    
    #removing the 0b prefix from the input
     IEEE_754_decimal = IEEE_754[2:]
     
     #extracting the sign, exponent and mantissa from the input
     sign = IEEE_754_decimal[0]
     exponent = IEEE_754_decimal[1:6]
     mantissa = IEEE_754_decimal[6:16]
     
     #converting exponent from binary to decimal
     exp_decimal = bin2dec(exponent)
     
     #ubias the exponent by subtracting 15
     exp_unbiased = exp_decimal - 15
     
     
     sign_value = (-1) ** int(sign)
     
     #converting the mantissa to a decimal
     decimal_mantissa = bin2dec(mantissa)
     final_mantissa = 1 + (decimal_mantissa / (2 ** 10))
     
     #Evaluating special cases
     #if both the exponent and mantissa are both zero we must return 0.0
     if exponent == "00000" and mantissa == "0000000000":
         return 0.0
         
     #dealing with subnormal numbers    
     elif exponent == "00000" :
         final_mantissa = decimal_mantissa / (2 ** 10)
         return sign_value * (2 ** -14) * final_mantissa
         
     #determine whether it is nan or infinity         
     elif exponent == "11111":
         #if mantissa is comprised of all zeros 
         #then it must represent either positive or negative infinity
         if mantissa == "0000000000":
             if sign == "0":
                 return float('inf')
             else:
                 return float('-inf')
        
         return float('nan')
         
     #final conversion   
     return sign_value * (2 ** exp_unbiased) * final_mantissa
    



    