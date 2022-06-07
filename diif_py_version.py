from subprocess import Popen
import os
#with open('my.bat','w+') as bat:
    #bat.write("py -3.9 -m venv ENV39")
    #bat.write("py -3.10 -m venv ENV310")
    #bat.write(".\\ENV39\\Scripts\\activate")
    #bat.write("python -V")
    #bat.write("deactivate")
   # bat.write(".\\ENV310\\Scripts\\activate")
    #bat.write("python -V")

p=Popen(r'py -3.9 -m venv ENV39')
p310=os.system(r'py -3.10 -m venv ENV310')
#Popen(r'.\\ENV39\\Scripts\\activate')
#Popen(r'python -V')
a=os.getcwd()
print(a)
os.chdir(r'.\\ENV39\\Scripts')
#os.system(r'activate')
os.system(r'python -V')
os.system(r'deactivate')
os.chdir(a)
print(os.getcwd())
os.system(r'python -V')
