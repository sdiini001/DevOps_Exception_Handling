# basic structure
# exception are classes that can be thrown and pulled

try:
    # this is where our desired code goes
    print("This is the TRY block")
    file_object = open('foo', 'x')
  #   x = 10 / 0


except FileNotFoundError as ex:
    # this will catch the specific exception
    print("This file cannot be found", ex.filename)
    print("This is the except block")
    # in other languages this is s CATCH block

# we can have mutiple except blocks
except FileExistsError as ex:
    print("This file already exists", ex.filename)
    print("This is another EXCEPT block")

except Exception as ex:
    print("This will catch anything")
    print(type(ex))

finally:
    print("This is the FINALLY block. It will always run.") # it will run if there is or isn't an exception
    print("It's used for tidying up")