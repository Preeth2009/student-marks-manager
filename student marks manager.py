

b={}
def prog1(b):
    c=input("Enter student name:")
    d=int(input("Enter student marks:"))
    b[c]=d
    print("Student added successfully!")

def prog2(b):
    if len(b)!=0:
        print("----- Student List -----")
        print()
        if len(b)!=0:
            for i,j in b.items():
                print("Name :",i)
                print("Marks :",j)
                print()
    else:
        print("No students found.")

def prog3(b):
    if len(b)!=0:
        print("----- Topper -----")
        print()
        c=[]
        for i in b.values():
            c.append(i)
        c.sort()
        d=c[-1]
        e=''
        for i,j in b.items():
            if j==d:
                e=i
            else:
                pass
        print("Name :",e)
        print("Marks :",d)
    else:
        print("No students found.")

def prog4():
    print("Thank you for using Student Marks Manager.")

while True:
    print("===== Student Marks Manager =====")
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Find Topper")
    print("4. Exit")
    print()
    a=int(input("Enter choice:"))
    if a==1:
        prog1(b)
    elif a==2:
        prog2(b)
    elif a==3:
        prog3(b)
    elif a==4:
        prog4()
        break
    
    

    
    
