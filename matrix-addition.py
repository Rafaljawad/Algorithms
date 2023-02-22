#Python program to implement matrix addition
#split method returns a list of strings like so:
input1=input("enter your first list separated by ,: ").split(",")#['10', '20', '30']

#by using list(map)will convert it from list of string to list of int
matrix1=list(map(int,input1))#[10, 20, 30]
# def matrix_addition(m1,m2):
print(matrix1)


input2=input("enter your second list separated by ,: ").split(",")#['10', '20', '30']
#by using list(map)will convert it from list of string to list of int
matrix2=list(map(int,input2))#[10, 20, 30]
print(matrix2)

def matrix_addition(m1,m2):
    return m1+m2

print(matrix_addition(matrix1,matrix2))#o/p [10, 20, 30, 10, 20, 30]