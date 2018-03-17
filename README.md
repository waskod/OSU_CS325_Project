# OSU CS325 Traveling Salesman Project | Group 44
This is our groups implementation of the traveling salesman problem.

*******
Please Note, we have two seperate algorithms and files.
  1. 2-opt.py
  2. NearestNeighbor.py
*******

The test files were run by the following programs:

Unlimited Time
tsp_example_1.txt -- 2-opt.py
tsp_example_2.txt -- 2-opt.py
tsp_example_3.txt -- NearestNeighbor.py

test-input-1.txt  -- 2-opt.py
test-input-2.txt  -- 2-opt.py
test-input-3.txt  -- 2-opt.py
test-input-4.txt  -- 2-opt.py
test-input-5.txt  -- 2-opt.py
test-input-6.txt  -- 2-opt.py
test-input-7.txt  -- NearestNeighbor.py



Instructions:

2-opt.y:
  To run this program, place the script in your directory of choice along with the input text file
  run the program with the command:
  $ python 2opt.py -<number of cycles> <file name>
    the number of cycles is a paramater you can specify when running the program.
    it is not recomended to select a number greater than 3 for the cycle count
    as the number of cycles increases, the accuracy of the solution will increase
    however, it will negatively impact the runtime of the program

    if the number of cycles is not specified, the program will default to 3

    Example:

    $ python 2opt.py -2 inputFile.txt
 
 NearestNeighbor.py
  To run this program, place in directory with input file.  
  Takes 1 argument which is input file name i.e.:
  
  $ python NearestNeighbor.py <input file>
  
  
