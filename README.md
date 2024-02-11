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
└── python
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

-`input.txt`:This file

-`result.txt`:

py:

-`data.py`:

-`indata.py`:

-`main.py`:

-`tool.py`:


