names = []
votes = []
total_valid_votes = 0

# Εισαγωγή συνδυασμών και ψήφων
while True:
    name = input("Δώσε το όνομα του συνδυασμού ή κενή συμβολοσειρά για ολοκλήρωση της εισαγωγής συνδυασμών: ")
    
    if name == "":
        break
    
    try:
        votes_count = int(input(f"Δώσε τον αριθμό των ψήφων του συνδυασμού {name}: "))
        if votes_count < 0:
            print("Ο αριθμός των ψήφων πρέπει να είναι μη αρνητικός.")
            continue
        names.append(name)
        votes.append(votes_count)
        total_valid_votes += votes_count
    except ValueError:
        print("Παρακαλώ δώστε έναν ακέραιο αριθμό για τις ψήφους.")

# Εισαγωγή λευκών και άκυρων ψηφοδελτίων
white_votes = int(input("Δώσε τον αριθμό των λευκών ψηφοδελτίων: "))
invalid_votes = int(input("Δώσε τον αριθμό των άκυρων ψηφοδελτίων: "))

# Υπολογισμός ποσοστών
white_percentage = (white_votes / (total_valid_votes + white_votes + invalid_votes)) * 100
invalid_percentage = (invalid_votes / (total_valid_votes + white_votes + invalid_votes)) * 100
percentages = [(names[i], (votes[i] / total_valid_votes) * 100) for i in range(len(names))]

# Εκτύπωση ποσοστών
print(f"Τα λευκά ψηφοδέλτια ανέρχονται στο {white_percentage:.2f}% των ψηφοδελτίων.")
print(f"Τα άκυρα ψηφοδέλτια ανέρχονται στο {invalid_percentage:.2f}% των ψηφοδελτίων.")
print("Αποτελέσματα επί των εγκύρων ψηφοδελτίων:")

# Ταξινόμηση και εκτύπωση αποτελεσμάτων
percentages.sort(key=lambda x: x[1], reverse=True)
for name, percentage in percentages:
    print(f"{name}: {percentage:.2f}%")

# Έλεγχος για τον νικητή ή τον δεύτερο γύρο
if percentages[0][1] > 43:
    print(f"Ο συνδυασμός '{percentages[0][0]}' επικράτησε και εκλέγει δήμαρχο")
else:
    print("Δεν εκλέγεται δήμαρχος από τον πρώτο γύρο.")
    print("Στον δεύτερο γύρο θα συμμετάσχουν οι πλειοψηφίσαντες συνδυασμοί:")
    print(f"1. {percentages[0][0]} με ποσοστό {percentages[0][1]:.2f}%")
    print(f"2. {percentages[1][0]} με ποσοστό {percentages[1][1]:.2f}%")
