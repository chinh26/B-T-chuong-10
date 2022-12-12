import math
x = int ( input ( ' nhập x vào: '))
n = int ( input ( ' nhập n vào: '))
A =  pow ( (pow ( x, 2 ) + x + 1 ), n )  + pow ( ( pow ( x, 2 ) - x + 1 ), n ) 
print ( ' giá trị tính đc là: ', A )