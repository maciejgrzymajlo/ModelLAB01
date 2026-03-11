Opis kodu 
TworzenieModeliML.py
Tworzy model, który rozpoznaje gatunki irysów na podstawie wymiarów ich płatków i działek kielicha. Program uczy się na 80% danych, a następnie sprawdza swoją skuteczność na pozostałych 20%. Na koniec zapisuje wytrenowany model do pliku model_v1.joblib.
WczytajModel.py
Wczytuje wcześniej zapisany model i używa go do przewidzenia gatunku irysa na podstawie nowych, przykładowych danych (tutaj: irys o wymiarach 5.1, 3.5, 1.4, 0.2). Program zwraca numer klasy (0, 1 lub 2), do której należy kwiat.


Odpowiedź do zadania 5
Szybkość działania
Deweloperskie: Model może myśleć nawet kilka sekund bo nikomu to nie przeszkadza.
Produkcyjne: Model musi działać błyskawicznie

Dostępność
Deweloperskie: Model działa tylko lokalnie.
Produkcyjne: Model musi być dostępny 24/7 dla wielu użytkowników

Aktualność modelu
Deweloperskie: Raz nauczony model jest zapisywany do pliku.
Produkcyjne: Dane się zmieniają więc model z czasem staje się mniej dokładny


link do repozytorium
https://github.com/maciejgrzymajlo/ModelLAB01




Monitorowanie
Deweloperskie: Sam sprawdzam czy model działa.
Produkcyjne: Musi być system, który sprawdza czy model działa poprawnie
