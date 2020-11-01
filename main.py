import random
prenomsmen = ['Abel','Adam','Georgi','Iakob','Arsen','Luca','Narek','Iuri','Konstantine','Ramaz','Niko','Gabriel','Davit','Artur']
prenomswomen = ['Aghavni','Almast','Ana','Anastasia','Elene','Etri','Eva','Irina','Lia','Maia','Marina','Svan','Yeva',]

for x in range(54,64):
	print(x,"= {\n\tname = \"dynn_\"\n\tculture = \"avar\"\n}")

count = 2300002
for x in range(54,64):
	numfather = count
	count+=1
	nummother = count
	count+=1
	print(numfather, "= {\n\tname =",'"'+random.choice(prenomsmen)+'"','\n\treligion = "tengri_pagan"\n\tculture = "avar"\n\tdynasty = '+str(x)+'\n\t'+str(random.randint(1265,1305))+'.'+str(random.randint(1,12))+'.'+str(random.randint(1,29)),"= {\n\t\tbirth = yes\n\t}\n\t"+str(random.randint(1320,1350))+"."+str(random.randint(1,12))+"."+str(random.randint(1,29)),"= {\n\t\tdeath = yes\n\t}\n}\n")
	print(nummother, "= {\n\tname =",'"'+random.choice(prenomswomen)+'"','\n\treligion = "tengri_pagan"\n\tculture = "avar"\n\tdynasty = '+str(x)+'\n\tfemale = yes'+'\n\t'+str(random.randint(1265,1305))+'.'+str(random.randint(1,12))+'.'+str(random.randint(1,29)),"= {\n\t\tbirth = yes\n\t}\n\t"+str(random.randint(1320,1350))+"."+str(random.randint(1,12))+"."+str(random.randint(1,29)),"= {\n\t\tdeath = yes\n\t}\n}\n")
	for y in range(random.randint(1,10)):
		if random.randint(1,2)  == 1:
			print(count, "= {\n\tname =",'"'+random.choice(prenomswomen)+'"','\n\treligion = "tengri_pagan"\n\tculture = "avar"\n\tdynasty = '+str(x)+'\n\tfemale = yes'+f'\n\tfather = {numfather}\n\tmother = {nummother}'+'\n\t'+str(random.randint(1265,1305))+'.'+str(random.randint(1,12))+'.'+str(random.randint(1,29)),"= {\n\t\tbirth = yes\n\t}\n\t"+str(random.randint(1320,1350))+"."+str(random.randint(1,12))+"."+str(random.randint(1,29)),"= {\n\t\tdeath = yes\n\t}\n}\n")
		else:
			print(count, "= {\n\tname =",'"'+random.choice(prenomsmen)+'"','\n\treligion = "tengri_pagan"\n\tculture = "avar"\n\tdynasty = '+str(x)+'\n\t'+str(random.randint(1265,1305))+'.'+str(random.randint(1,12))+'.'+str(random.randint(1,29)),"= {\n\t\tbirth = yes\n\t}\n\t"+str(random.randint(1320,1350))+"."+str(random.randint(1,12))+"."+str(random.randint(1,29)),"= {\n\t\tdeath = yes\n\t}\n}\n")
		count+=1
	print('\n')