import pywhatkit as pw

txt="""What is Python in brief?
Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis. Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn't specialized for any specific problems. """

pw.text_to_handwriting(txt,"demo.png",[0,0,138])
print("end ")