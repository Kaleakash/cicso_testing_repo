a=10
b=1
dic = {"a": a, "b": b}
try:
    result = a / b
    print(result)
    print(dic["b"])
except Exception as e:
    #print("Division by zero is not allowed")
    print("Exception details:", e)
finally:
        print("Executing finally block")
        print("this code execute 100% sure - help to close the resources like files, network connections, etc.")

print("Normal Statement1")
print("Normal Statement2")
print("Normal Statement3")