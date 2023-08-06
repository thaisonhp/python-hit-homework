import math
# bai 1
# a
# print("Nhap vao so nguyen duong :" , end=" ")
# a = int(input())
# tong = 0
# while a > 0 :
#     b = a % 10
#     tong += b
#     a /= 10
#
# print("tong cac chu so vua nhap la: ",int(tong))

# cau b
# print("Nhap vao mot so nguyen duong:",end=" ")
# a = int(input())
# check = 0
# for i in range(2,int(math.sqrt(a)+1)):
#     if(a % i == 0):
#         check = 1
#         break
# if check == 0 :
#     print(("so vua nhap khong la so nguyen to"))
# else:
#     print("So vua roi la so nguyen to")

# cau c
# print("Nhap vao mot so nguyen duong:",end=" ")
# a = int(input())
# tong = 0
#
# for i in range(1,int(math.sqrt(a)+1)):
#     if a % i == 0:
#         tong += i
#         tong += a/i
#
# print("Tong cac uoc cua so nguyen duong la : ",int(tong))
# -------------------------------------------------------------
# cau 2
# print("Nhap so nguyen a :",end=" ")
# a = int(input())
# print("Nhap so nguyen b :",end=" ")
# b = int(input())
#
# print(f'{a} + {b} = {a+b}')
# print(f'{a} - {b} = {a-b}')
# print(f'{a} * {b} = {a*b}')
# print(f'{a} / {b} = {a/b}')
# print(f'{a} ** {b} = {a**b}')
# print(f'{a} % {b} = {a%b}')
# if a > b :
#     print("a > b")
# elif a == b:
#     print("a = b")
# else:
#     print("a < b")
# print(a and b)
# print(a or b)
# print(a != b)
# a+= 1
# print("a sau khi dich phai 1 don vi:", a)
# a -= 2
# print("a sau khi dich trai 1 don vị: ",a)


# phan 2 van dung

# cau 3
# cau a
# print("Nhap n:",end=" ")
# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s += i
# print("S(n) =", s)

# cau b
# print("Nhap n:",end=" ")
# n = int(input())
# s = 0
# tu = 1
# mau = 1
# for i in range(1,n+1):
#     s += tu/mau
#     mau += 1
# print("S(n) =", s)

# cau c
#
# print("Nhap vao he so cua phuong trinh : a*x^2 + b*x + c = 0")
# print("a =", end=" ")
# a = int(input())
# print("b =", end=" ")
# b = int(input())
# print("c =", end=" ")
# c = int(input())
# if a == b and b == 0 :
#     if c == 0 :
#         print("Phuong trinh vo so nghiem")
#     else:
#         print("Phuong trinh vo nghiem")
# elif a == 0 and b != 0:
#     print("Phuong trinh co nghiem duy nhat: ",-c/b)
# elif a != 0 and b != 0:
#     delta = b**2 - 4*a*c
#     if delta < 0 :
#         print("Phuong trinh vo nghiem")
#     elif delta == 0:
#         print("Phuong trinh co nghiem kep: x =", -b/(2*a))
#     else:
#         x1 = (-b - math.sqrt(delta))/(2*a)
#         x2 = (-b + math.sqrt(delta))/(2*a)
#         print("Phuong trinh co 2 nghiem phan biet:")
#         print("x1 =", x1)
#         print("x2 =", x2)

# ---------------------------------------------------------------------
# cau 4
# print("So fibonaci thu :", end=" ")
# n = int(input())
# if n == 0 :
#     print("so fibonaci thu 0 la: 0")
# elif n == 1:
#     print("So fibonaci thu 1 la: 1")
# else:
#     n0 = 0
#     n1 = 1
#     f = 0
#     for i in range(2,n+1):
#         f = n0 + n1
#         n1 = f
#         n0 = n1
#     print("So fibonaci thu", n," la: ",f)

# ------------------------------------------------------------------
# def sumNumber(a):
#     tong = int(0)
#     while a >= 1 :
#         b = int(a % 10)
#         tong += int(b**3)
#         a = int(a / 10)
#     return tong
# def isAmstrong(a):
#     if(sumNumber(a) == a):
#         return 1
#     else:
#         return 0
#
# print("Nhap so nguyen n: ", end=" ")
# n = int(input())
# cnt = 0
# for i in range(0,n+1,1):
#    if(isAmstrong(i) == 1):
#        cnt = 1
#        print(i)
# if cnt == 0:
#     print("Khong co so amstrong nao")
# ------------------------------------------------
# bai 6

# def tongUoc(a):
#     tong = 0
#     for i in range(1,int(math.sqrt(a))+1):
#         if(a % i == 0):
#             tong += i
#             b = int(a/i)
#             if b != i and b != a:
#                 tong += int(a/i)
#
#     return tong
#
# def isPerfectNumber(a):
#     if(tongUoc(a) == a):
#         return 1
#     else:
#         return 0
#
# print("Nhap so nguyen n:",end=" ")
# n = int(input())
# cnt = 0
# for i in range(1,n+1):
#     if(isPerfectNumber(i) == 1):
#         print(i, end=" ")
#         cnt = 1
#
# if cnt == 0:
#     print("Khong co so hoan hao tu 1 den n!")
# /---------------------------------------------

# bai 7 : bài 3 em không chỉ biện luận mà giải luôn rồi nên bài này thôi em không giải nữa

# bai 8
# def tongUoc(a):
#     tong = 0
#     for i in range(1,int(math.sqrt(a))+1):
#         if(a % i == 0):
#             tong += i
#             b = int(a/i)
#             if b != i :
#                 tong += int(a/i)
#     return tong
#
# print("Nhap so nguyen n:",end=" ")
# n = int(input())
# i = 1
# while tongUoc(i) <= n:
#     print("Cap so Amicable la:", i," ",tongUoc(i))
#     i += 1

# bai 6.2

# print("Nhap so nguyen N:",end=" ")
# n = int(input())
# for i in range(1,n+1): #hang
#     for j in range(1,2*n): #cot
#         if j > 5 - i and j < 5 + i  :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print("")

# bai 9
# print("Nhap so nguyen a:",end=" ")
# a = int(input())
# cnt = 0
# while a > 0 :
#      a = int(a/2)
#      cnt += 1
# print("Số bit cần để biểu diễn a ở dạng nhị phân là: ",cnt)