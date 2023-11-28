
def start():
     str = 'welcome to the python learning program'


    #  print( "welcome"  not in str)
    #  print("python" in str)
    #  print(str[:7])
    #  print(str[7:25]) # to get the data b/w range of string
    #  print(str[-8:]) # get data from end of string
    #  print(str[:-8])

def stop():
     strStop = "Say hello to python"

    #  if "Say" in strStop: # to check string contain the char
    #       print(strStop)
    
    #  if len(strStop):
    #       print('string have the char count') # to check the string char count

    #  dataString = "Here you can check all type of if else condition"

    #  if "Here" not in dataString:
    #       print('Here is include in data string')
    #  elif len(dataString) < 0:
    #       print('string is grater then 0')
    #  else:
    #       print('default value of string')
def inputOperation():
     print("Perform input operation here")
     name = input("Enter you name here:\t")
     print(name)
    
    

if __name__=="__main__":
    start()
    stop()
    inputOperation()