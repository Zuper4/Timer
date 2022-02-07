print("\nThis program is able to print how much time the code was executed.")
print("Feel free to paste your code bettween the variable start and end.")

from timeit import default_timer as timer

start = timer()

# Your code...

end = timer()

print(end - start)

