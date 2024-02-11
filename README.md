# Solution-of-Sudoku

The program is aim to solve sudoku. With tested by some sudoku softwares, this program can solve no more than 30 seconds.  The program includes 4 texts for configuation and IO, and 4 python codes to support the program. The exe folder is the result of using pyinstaller to convert the code to software; The python folder is the source code.Below is the file structure

```
main
|
├── exe
|    ├── _internal
|    |    └── ...
|    ├── config.txt
|    ├── data.txt
|    ├── input.txt
|    ├── main.exe
|    └── result.txt
└── python code
     ├── config.txt
     ├── data.py
     ├── data.txt
     ├── indata.py
     ├── input.txt
     ├── main.py
     ├── result.txt
     └── tool.py
```

## Description of the Files in Python Folder

txt:  

-`config.txt`: It contains the dictionary that save the format and file path. For example, {"n":9,"boxsize":3,"path":"xxx/data.txt","input_path":"xxx/input.txt","save_path":"xxx/result.txt","input_class":1}. If there 's nothing, the program will choose its default format and path. Attention, if input_class is 1, the program will get the puzzle from input.txt; while if input_class is 0, the program will get the puzzle from data.txt.

-`data.txt`: It contains the data of the puzzle. This file records the puzzle by save the gived value by coordinate in the 2d list and the topleft is (0,0).For example, [[0,1,7],[0,4,6],[1,0,3],[1,3,5],[2,0,2],[2,2,4],[2,4,9],[2,8,3],[3,4,4],[3,5,6],[3,7,1],[3,8,8],[4,1,4],[4,3,3],[4,7,7],[5,4,5],[5,5,7],[5,7,2],[5,8,9],[6,0,9],[6,2,6],[6,4,3],[6,8,5],[7,0,8],[7,3,4],[8,1,1],[8,4,2]]

-`input.txt`:This file saves the puzzle in a direct way. For example:
```
0 0 0	9 0 0	0 0 0
8 0 0	4 7 6	0 0 9
0 0 4	8 0 0	1 0 6

7 9 5	0 0 0	0 1 0
0 0 0	0 0 3	0 0 0
3 4 1	0 0 0	0 9 0

0 0 6	2 0 0	3 0 7
1 0 0	7 6 8	0 0 2
0 0 0	3 0 0	0 0 0
```
we divide each grid by tab and carriage return, separate each number in the same grid by blank space, and replace the blank with 0

-`result.txt`: It saves the solution of the puzzle in the same format as it in the `input.txt`

py:

-`data.py`: It stores default configuration. If `config.txt` is blank, we'll use this file's data.

-`indata.py`: It is used to load the configuration and the puzzle. It includes 4 functions--`config`, `Input_data`, `Indata`, `Transform_data`. We firstly load configuration in `data.py`. The function `config` loads `config.txt` to upgrade if it is not blank. The function `Indata` loads puzzle by coordinate in `data.py`. The function `Transform_data` loads puzzle in `input.txt`. The function `Input_data` checks input_class to choose the way we will load.

-`main.py`: It is the main code. We load the basic configuration and puzzle from `indata.py` at first. It contains 11 functions divided into 2 classes -- for output and for solution.  
For output:
--`list_str`: The result is saved in 2d-list. For beautiful output, we use this function to transform the list into a suitable string. Such string will be printed just as we fill in the `input.txt`
--`r_print`: It aims to print the string that is transformed from the list by function `list_str`.
--`zero`: Because of the algorithm， if we cannot solve but still want to get the puzzle we have filled, at this time the list is 3d-array beacuse it contains some lists of choices that we can fill in the blank. This function is to replace these lists with 0 for beautiful output.
--`save`: It saves the result in the file with the path we have set.
For solution:
--`solve`: It contains the main loop of the algorithm.
--`operation`: In one loop all of operations are in this function
--`update_out`: It is used to clear the choice so we wouldn't fill too many the same numbers by check and upgrade a special array.
--`magic`: It aims to simplify and leave out some assumption.
--`hypothesis`: 
--`subhypothesis`: 
--`simple_check`: 

-`tool.py`:


