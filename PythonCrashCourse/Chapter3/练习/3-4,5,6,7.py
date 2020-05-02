#3-4
# the person I'd like to invite to have dinner with me.
invited_person = ['Mite', 'Mike', 'Bryce', 'Juli', 'Lynette', 'Malfoy']
for name in invited_person:
    print('Hi, ' + name + " I ask you for dinner.")
print('_' * 30)  #打印下划线,用来隔开数据


#3-5
#显示谁谁不能来
print("it's a pity that " + invited_person[-1] + " can't come with us")
print('_' * 30)

invited_person[-1] = 'Dombledore'#更换不能来的人名为另一个名字

for name in invited_person:#用for语句给每一个人发信息
    print('Hi, ' + name + " I ask you for dinner.")
print('_' * 30)

#3-6
print("Hi, everyone. I have found out a bigger table to hold more people.")
print("So I'll invite another three people")
print('_' * 30)

#添加三个人到列表
invited_person.insert(0, 'Hermione')
invited_person.insert(3, 'Harry')
invited_person.append('Ron')

#给列表内的人发消息
for name in invited_person:
    print('Hi, ' + name + " I ask you for dinner.")
print('_' * 30)

#3-7

new_invited_person = []#建立新的列表,最后决定邀请的人

print("I have to apologize to you for the table's not arriving on time to hold just two people. I'm sorry.")

#将被邀请的两个人添加到新列表
new_invited_person.append(invited_person.remove('Harry'))
new_invited_person.append(invited_person.remove('Juli'))

#给旧名单(未被邀请)发信息
for name in invited_person:
    print(name.title() + ", I'm apologize to you for not inviting you for dinner because of the table's being small")
print('_' * 30)

#给新列表中的人发信息
for names in new_invited_person:
    print(name.title() + ", I can just invite two people for dinner, and you are one of then.")
