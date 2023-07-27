import platform
import getpass


def hello():    
    python_name = platform.python_implementation()
    os_name = platform.system()
    environment_username = getpass.getuser()
    username = input("Enter your name: ")
    if python_name == "PyPy":
        explain_python = "A fast and efficient implementation of Python in Python (a just-in-time compiler),"
    elif python_name == "CPython":
        explain_python = "The standard implementation of Python written in C (the most common one),"
    elif python_name == "IronPython":
        explain_python= "An implementation of Python for .NET framework,"
    elif python_name == "Jython":
        explain_python = "An implementation of Python for the Java Virtual Machine (JVM),"
     
    print(f"Hello {username}! You are using {python_name}, {explain_python} on {os_name} in os user {environment_username}.")

if __name__ == "__main__":
    hello()