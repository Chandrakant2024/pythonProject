# Match Statement --- swtch in java
# match the top and execute
# Python > 3.10


# Write a program to ask the user which browser he wants to run automation.

browser_name = input("Enter the browser name\n")
match browser_name:
    case "firefox":
        print("Starting firefox!!!!")
    case "chrome":
        print("Execute chrome code!!!!")
    case "edge":
        print("Execute edge code!!!!")
    case "safari":
        print("Execute safari code!!!!")
    case "bing":
        print("Execute bing code !!!!")
    case _:                                                     # default is printed other than the selected browsers in the list
        print("Browser not found!")
