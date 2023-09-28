
Curriculum
Short Specializations
Average: 177.41%
We're moving to Discord!
In a few days, we will be leaving Slack in favor of Discord 🎉
Click here for more information
0x00. Pascal's Triangle
Algorithm
Python
 By: Alexa Orrico, Software Engineer at Holberton School
 Weight: 1
 Project will start Sep 25, 2023 6:00 AM, must end by Sep 29, 2023 6:00 AM
 Checker was released at Sep 26, 2023 6:00 AM
 An auto review will be launched at the deadline
Concepts
For this project, we expect you to look at this concept:

Technical interview
Tasks
0. Pascal's Triangle
mandatory
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
