name = str(input ('Hi, user please can you enter your name:'))
text_file = open("Output.txt", "w")
text_file.write(name)
text_file.close()