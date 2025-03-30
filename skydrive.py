a=1
b=2
c=10086
print("hello world",a,b,c)
# while c>10000:
#     if a == 1:
#         print(c)
#         c=c-1
#     else:
#         print(b)



for i in range(10):
    print(i)

test_list=[]
list1=[1,2,3]
list2=['a',b,b]
test_list.append(list1)
test_list.append(list2)
print(test_list)

matrix_test=[[11,22,33],[11,22,33],[11,22,33]]
for i in range(len(matrix_test)):
    for j in range(len(matrix_test[0])):
        matrix_test[i][j]=i+j*0.1

for i in range(len(matrix_test)):
    for j in range(len(matrix_test[0])):
       print(matrix_test[i][j])
print(matrix_test)
