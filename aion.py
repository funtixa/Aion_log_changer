
with open('Chat.log')as g:
    line = g.readline()
    for line in g:
        newdata = line.replace("through the effect of", "by using")
        file = open('Chat2.log', 'a+')
        file.write(newdata)
file.close()

with open('Chat2.log')as g:
    line = g.readline()
    for line in g:
        newdata = line.replace("through to the effect of", "by using")
        file = open('Chat3.log', 'a+')
        file.write(newdata)
file.close()
