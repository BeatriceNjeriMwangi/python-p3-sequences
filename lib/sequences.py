#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    a,b = 0,1

    for i in range(length):
        fibonacci_sequence.append(i)
        a,b =b, a+b
    print(fibonacci_sequence)
    
print_fibonacci(9)