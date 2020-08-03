"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
f = open(r'C:\Users\lesle\Desktop\lambda\CS Unit 1 Sprint 1\Intro-Python-I\src\foo.txt', 'r')
# YOUR CODE HERE
with open(r'C:\Users\lesle\Desktop\lambda\CS Unit 1 Sprint 1\Intro-Python-I\src\foo.txt') as f:
    read_data = f.read()

read_data


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
w = open(r'C:\Users\lesle\Desktop\lambda\CS Unit 1 Sprint 1\Intro-Python-I\src\bar.txt', 'w')
w.write("arbitrary content # 1 \n")
w.write(str(13))
w.write("arbitrary content 3 \n")
w.close

# YOUR CODE HERE