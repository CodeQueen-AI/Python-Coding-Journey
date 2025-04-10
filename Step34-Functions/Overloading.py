class Example:
    def show(self, *args):
        if len(args) == 1:
            print(f"One parameters {args[0]}")
        elif len(args) == 2:
            print(f"Two parameters: {args[0]}, {args[1]}")
        else:
            print("Invalid number of arguments")

obj = Example()
obj.show(10) 
obj.show(10, 20) 
