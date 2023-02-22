# my way to solve it 
# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

number_of_students=int(input("enter the number of student to calculate their scores: "))
student_list=[]
score_list=[]
for i in range(number_of_students):
    name=input("enter name: ")
    score=float(input(f"enter {name}'s score: "))
    student_list.append([name,score])
    score_list.append(score)
print(student_list,score_list,sep="--------")
#first extract the min1 to remove it 
min1=min(score_list)
#then make an empty list to append all items that are not equal to min1 just in case we have duplicate values of min1(if we have two min values like 10 and in thi case will get rid of both throgh this condition)
score_list2=[]
for x in range(len(score_list)):
    if (score_list[x]!=min1):
        score_list2.append(score_list[x])
print(score_list2)
#now the new list has no min value , now we can extract the min value from the new list (in this case this min2 will be the second min bcause we removed the first min )
min2=min(score_list2)
print(min2)
#now will create an empty list that has names associated with min2 values
minimum_score_names=[]
#loop through the new list that has no min1 value and compare it with min2 
for i in range(len(student_list)):
    #if the score ==min2 , then bring the names and append them into new list 
    if(student_list[i][1]==min2):
        minimum_score_names.append(student_list[i][0])
        # print(student_list[i][0])
#now sort them alphapetically 
minimum_score_names.sort()
for l in minimum_score_names:
    #loop throgh the sort list to display the names in order
    print(l)






#****************************submitted on hacker rank********************
# if __name__ == '__main__':
#     student_list=[]
#     score_list=[]
#     n=int(input())
#     for _ in range(n):
#         name = input()
#         score = float(input())
#         student_list.append([name,score])
#         score_list.append(score)

#     min1=min(score_list)
#     score_list2=[]
#     for x in range(len(score_list)):
#         if (score_list[x]!=min1):
#             score_list2.append(score_list[x])
#     # print(score_list2)
#     min2=min(score_list2)
#     # print(min2)
#     minimum_score_names=[]
#     for i in range(len(student_list)):
#         if(student_list[i][1]==min2):
#             minimum_score_names.append(student_list[i][0])
#         # print(student_list[i][0])
#     minimum_score_names.sort()
#     for l in minimum_score_names:
#         print(l)
