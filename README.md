# OSU CS325 Traveling Salesman Project | Group 44
This is our groups implementation of the traveling salesman problem.

Instructions:

To run this program, place the script in your directory of choice along with the input text file
run the program with the command:
$ python tsp.py -<number of cycles> <file name>
  the number of cycles is a paramater you can specify when running the program.
  it is not recomended to select a number greater than 3 for the cycle count
  as the number of cycles increases, the accuracy of the solution will increase
  however, it will negatively impact the runtime of the program
  
  if the number of cycles is not specified, the program will default to 3
  
  Example:
  
  $ python tsp.py -2 inputFile.txt
