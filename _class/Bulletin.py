import constants
from helpers.functions import symbole

class Bulletin:

    
    def __init__(self):

        self.students = []
        self.total_students = 0
        self.students_copy = []
        self.start()

    def start(self):
        
        while True:

            choice = int(input(constants.CHOICE_MESSAGE))

            if (choice == 1): self.saveStudents()
        
            if (choice == 2): self.searchStudent()

            if (choice == 3): self.showStatistics()

            if (choice == 4): self.printStudent()

            if (choice == 0):

                print("\nBye!")
                exit(1)

    def saveStudents(self):
        
        self.total_students = int(input("Entrer le nombre total d'etudiants : "))

        for i in range(self.total_students):

            currentStudent = {}
            currentStudent['lastname'] = input("Entrer le nom de l'etudiant : ")
            currentStudent['firstname'] = input("Entrer le prenom de l'etudiant : ")
            currentStudent['moyTotal'] = 0
            currentStudent['subjects'] = []

            for i in constants.SUBJECTS:

                note1 = int(input("Note 1 : "))
                note2 = int(input("Note 2 : "))
                moy = (note1 + note2) / 2
                currentStudent['subjects'].append([note1, note2, moy])
                currentStudent['moyTotal'] += moy

            currentStudent['moyTotal'] /= len(constants.SUBJECTS)
            currentStudent['mention'] = self.getMention(moy)

            self.students.append(currentStudent)

        self.students.sort(key = lambda student: student['lastname'])
        self.saveInFile()
        return self.showStatistics()


    def saveInFile(self):
        
        self.students_copy = self.students.copy()

        self.students_copy.sort(key = lambda student: student['moyTotal'], reverse = True)

        file = open("resume.txt", "w")

        with file:
            line = ""
            for student in self.students:

                line += f"{student['lastname']} {student['firstname']}\t"

                for i in student['subjects']:
                    line += f" {i} "
                
                line += f" { student['moyTotal'] } { student['mention'] } {str(self.students_copy.index(student) + 1)}e \n"

            file.write(line)


    def showStatistics(self):
        
        firstStudent = max(self.students, key= lambda student: student['moyTotal'])
        lastStudent  = min(self.students, key= lambda student: student['moyTotal'])
        
        symbole()
        print("\n- La plus forte moyenne est : " + str(firstStudent['moyTotal']))
        print("\n- La plus faible moyenne est : " + str(lastStudent['moyTotal']))
        symbole()

    
    def searchStudent(self):

        searchResult = self.getStudent()
        
        if searchResult:

            symbole()
            print("Etudiant trouve !\n")
            print(f"Nom : {searchResult['lastname']}\nPrenom : {searchResult['firstname']}\nMoyenne : {searchResult['moyTotal']}\nMention : {searchResult['mention']}\nRang: {str(self.students_copy.index(searchResult) + 1)}e")
            symbole()

            return True
            

        print("L'etudiant n'a pas ete trouve.\n")
        

    def getStudent(self):

        searchResult = False

        query = input ("Search for students : ")

        for i in range(self.total_students):

            if self.students[i]["lastname"] == query or self.students[i]["firstname"] == query:

                searchResult = self.students[i]

        return searchResult
    

    def printStudent(self):

        student = self.getStudent()

        if student:

            symbole(66, "o");
            print("o\t\t\t BULLETIN DE NOTES !");
            symbole(66, "o");
            print(f"\no Nom : { student['lastname']} \no Prenom : {student['firstname']}\n");
            print("o Matricule : 12412923\t\t\t\tAnnee : 22-23\n");
            print("o Licence : 1\t\t\t\t\tSemestre: 2");
            symbole(33, "--");
            print("o Matieres : ");
            for i in constants.SUBJECTS:
                print("\n" + i + "\t : ", end="\t");
                for j in student['subjects'][constants.SUBJECTS.index(i)]:
                    print(j, end="\t");
                
            symbole(33, "--");
            print(f"\no Moyenne Generale : {student['moyTotal']} \no Rang : {str(self.students_copy.index(student) + 1)}e\n")
            print(f"o Mention : {student['mention']} \t\t\t\tDecision : { self.decision(student['moyTotal']) }\n");
            symbole(66, "o");

            return True


        print ("Etudiant non trouve")

    
            
    def getMention(self, number) -> str:

        if number < 3: return "Nul"
        elif number >= 3 and number <= 6 : return  "Mediocre"
        elif number > 6 and number < 10 : return "Insufisant"
        elif number >= 10 and number < 12 : return "Passable"
        elif number >= 12  and number < 14 : return "Assez Bien"
        elif number >= 14  and number < 16 : return "Bien"
        elif number >= 16  and number < 18 : return "Tres Bien"
        elif number >= 18  and number <= 20 : return "Excellent"

    
    def decision(self, moy) -> str:

        if moy < 10:
            return "Redouble"
        
        return "Admis (e)"