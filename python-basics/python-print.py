print ("Hello, World")


##### syntax errors ##########
#if we were to capitalize the p in print it would cause a nameerror as Print isn't defined


#Print ("Hello,World")
#the error give will you info on where the error is  File "C:\Users\phunk\Documents\GitHub\python-practice\python-basics\python-print.py", line 4, in <module>
#    Print ("Hello,World")
#    ^^^^^
#NameError: name 'Print' is not defined. Did you mean: 'print'?
#in this case  we are told our error was on line 4 where we call Print

#what happens if we forget the trailing parenthasese?
# print ("Hello, World"
#you are greeted with a SyntaxError: '(' was never closed sometimes it might tell you unexpected EOF which basically means end of file or end of the line was reached and it found an error

# print ("Hello, World')
#SyntaxError: unterminated string literal (detected at line 18) basically means mismatched quotes quotes must be the same at the start and the end