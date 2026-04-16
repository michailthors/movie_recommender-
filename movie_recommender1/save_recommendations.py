import pandas as pd

# Παράδειγμα: φτιάχνουμε recommendations για μία ταινία
from main import recommend_movies  # αν θέλεις να χρησιμοποιήσεις τη συνάρτηση από το main.py

movie = "Toy Story (1995)"
result = recommend_movies(movie)

if isinstance(result, tuple):
    matched_title, recommendations = result
    # Δημιουργία DataFrame
    df = pd.DataFrame(recommendations, columns=["Recommended Movies"])
    # Προαιρετικά: βάζουμε και ποια ταινία ήταν η βάση
    df.insert(0, "Base Movie", matched_title)
    
    # Αποθήκευση σε CSV
    df.to_csv("sample_recommendations.csv", index=False)
    print(f"CSV με recommendations δημιουργήθηκε: sample_recommendations.csv")
else:
    print(result)  # Αν δεν βρέθηκε ταινία