persons = {
	1: "John",
	2: "Jane"
	}
	
def throughAll():
    for a, b in persons.items():
        print a, b
        
def find(searchValue):
    for a, b in persons.items():
        if searchValue in b:
            print a, b
            return
    print "not found"
            
find("Jane")