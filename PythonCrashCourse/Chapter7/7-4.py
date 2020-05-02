prompt = "\n请输入你想要的比萨配料: "
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print("我们会在比萨中添加它.")
