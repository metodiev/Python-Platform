def  catchException():

    try:
    
        piNumbers = [1,2,3,4]
        for i in range(1,41):
        
            print(piNumbers[i])
        
    except AssertionError as error:
        print(error)
        
    

print(catchException())

def  catchException():

    try:
    
        piNumbers = [1,2,3,4]
        for i in range(1,41):
        
            print(piNumbers[i])
        
    except AssertionError as error:
        print(error)
        
    
def finallyMethod():
    a = 5
    b = 2
    try:
        print("Try1")
        try:
            a1 = 5
            b1 = 2
            print("Try2")
            return (a1+b1)
        except:
            print("Catch 1")
        finally:
            print("Finally 1")
        return a+b    
    finally:
        print("Finally 2")
        return a + b+1000
    
print(catchException())

def  tryCatchFinally():
    try:
        sum = 100
        print("Try Block")
    except:
        print("This excpetion is not going to be executed")
    finally:
        print("The finally method is always executed")


tryCatchFinally()

def  unCheckedContext():
    a = 0
    b = 1000
    try:
        
        while(true):
            b+=1
            try:
                a+1
                p = int(126) + 1
                
                
            except Exception:
                traceback.print_exc()
    except Exception:
        print(a)
        print(b)
        

unCheckedContext()  


import traceback
def  stackOverflowException(sum):
    try:
        return stackOverflowException(sum)+ 1
    except Exception:
        traceback.print_exc()
        
    return sum    

stackOverflowException(5)



import traceback
import fileinput
import fileoutput
def  exceptionWithFile():
    
        in1 = open("test.txt","r+")
        out = open("test.txt","w+")
        while(in1.read() != -1):
            in1.write("This is line  %d\r\n")
        except Exception:
        traceback.print_exc()
        finally:
            if(in1.read() !=null):
                in1.close()
        if(out != null):
            out.close()

exceptionWithFile()
