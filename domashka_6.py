#Task30
#a1 = int(input())
#d = int(input())
#n = int(input())

#lst = [a1 + (i-1)*d for i in range (1,n+1)]
#print(lst)


#task31
#a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
#maxx = int(input())
#minn = int(input())
#lst = [indx for indx,val in enumerate(a) if minn<=val<=maxx]
#print(lst)


#task32
def pow_a_b(a,b,res):
if b==1:
return res
return pow_a_b(a,b-1,res*a)

a = int(input())
b = int(input())
res = a
print(pow_a_b(a,b,res))
