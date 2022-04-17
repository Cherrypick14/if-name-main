#   in this program we are going to learn how to use the __name__ == "__main__"
#   this is the main module so we are going to import another module
#    acts as the main script
import employee

print("executed successfully")

#   our program
def function_one():
    print("Function one executed successfully!")

def function_two(c):
    user_input=int(input("Enter a number: "))
    return c * user_input

    
if __name__ == "__main__":
    print("function one invoked correctly")
    print(function_two(6))
    function_one()
    employee.employee_one()

else:
    print("imported module executed correctly")
 

