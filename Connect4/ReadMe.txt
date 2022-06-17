	Projekt został wykonany przez Michała Laskowskiego

1. Użytkowanie:
	
	1. Uruchomienie programu: 
	
		Aby uruchomić program należy za pomocą interpretera pythona uruchomić plik o nazwie main.py
	
	2. Nowa gra: 
	
		Program pyta się czy użytkownik chce zacząć nową grę:
		- po wpisaniu 'n', 'N', 'no', 'No' lub 'NO' program wznowi zapisaną grę (jeżeli jest taka gra)
		- po wpisaniu 'h' lub 'H' program wyświetli maksymalnie 10 najlepszych dotychczas wyników graczy
		- każdy inny znak uruchomi nową grę i przejście dalej do kolejnego pytania

	3. Tworzenie planszy:
	
		Kolejne pytanie dotyczy zmiany wymiarów plaszy:
		- jeżeli użytkownik wpisze 'Yes', 'yes', 'YES', 'y' lub 'Y' program przejdzie do tworzenia planszy
			* tworzenie planszy polega na wpisaniu przez użytkownika odpowiednich wartości szerokości i wysokości (liczba od 4 do 9),
			  po czym program przejdzie dalej
		- każdy inny znak spowoduje stworzenie planszy o domyślnym rozmiarze (6 wysokości i 7 szerokości) i przejście dalej
	
	4. Wybór trybu gry: 
	
		Dalej następuje wybór trybu gry (gracz vs gracz lub gracz vs bot) poprzez zapytanie czy użytkownik chce rozegrać partię z botem:
		- jeżeli użytkownik wpisze 'n', 'N', 'no', 'No' lub 'NO' rozpocznie się gra dla dwóch graczy
		- każdy inny znak rozpocznie grę z przeciwnikiem komputerowym
	
	5. Gra:
		Gra polega na wyborze numeru kolumny (od 1 do wybranej szerokości) do której będzie 'wrzucony' token (1 lub 2 zależnie od gracza):
		(* w każdej chwili zamiast numeru kolumny użytkownik może wpisać 's' lub 'save', aby zapisać daną rozgrywkę)
		- token odpowiednio przenosi sie na ostatnie wolne miejsce na dole kolumny
		- należy tak dobierać kolumny aby nasze tokeny ułożyły się w linię czteroelementową (może być w pionie, poziomie lub diagonalnie)
		- po takim ułożeniu tokenów jednego gracza następuje komunikat o wygranej i przejście do zapisu wyniku
		- jeżeli została zapełniona cała plansza bez wygranego, gra kończy się remisem
	
	6. Zapis gry:
	
		Program wyświetli zapytanie czy użytkownik chce zapisać swój wynik:
		- jeżeli użytkownik wpisze 'Yes', 'yes', 'YES', 'y' lub 'Y', program poprosi o podanie nazwy i zapisze wynik bazujący na ilości tur do zwycięstwa
		- każdy inny znak przejdzie do zakończenia działania programu
		

2. Cele Projektu:

	Zaprojektowanie i zaimplementowanie w pełni funkcjonalnej gry Connect Four w interfejsie tekstowym:
		- tryb dla dwóch graczy
		- tryb z przeciwnikiem komputerowym (prosty bot)
		- możliwość zapisu i wczytania stanu gry
		- przechowanie listy najlepszych wyników graczy

3. Pliki:
	
	1. Podział na pliki źródłowe:
		- connect_4_Board_class.py	-> zawiera klasę Board odpowiadającą za planszę
		- connect_4_Game_class.py	-> zawiera klasę Game odpowiadającą za dokładny przebieg gry
		- connect_4_Bot_class.py	-> zawiera klasę Bot, której głównym zadaniem jest znalezienie numeru najlepszej dla przeciwnika kolumny
		- connect_4_Interface_class.py	-> zawiera klasę Interface, która odpowiada za pełną komunikację z graczem za pomocą interfejsu tekstowego (terminala)
		- connect_4_io.py		-> zawiera funkcje odpowiadające za zapis i odczyt z plikow zawierających informacje o zapisanej grze ('saved_game') lub wynikach ('best_scores')
		- connect_4_exceptions.py	-> zawiera klasy odpowiadające konkretnym wyjątkom użytym w innych plikach źródłowych
		- main.py			-> zawiera stworzenie obiektu interfejsu i wywołanie głównej jego metody

	2. Podział na pliki testowe:
		- test_connect_4_Board_class.py
		- test_connect_4_Game_class.py
		- test_connect_4_Bot_class.py

4. Implementacja:
	
	1. Klasy:

		- Board		->	Jako argumenty przyjmuje wartości wysokości i szerokości (domyślnie 6 i 7)
					Głównymi metodami są:
						- create_gameboard   ->	odpowiada za stworzenie pustej planszy (zawirejącej same 0) o podanych wymiarach
									plansza (gameboard) jest dwuwymiarową tablicą o odpowiedniej ilości pól
						- full_board	     ->	odpowiada za sprawdzenie czy na planszy jest jeszcze jakieś wolne pole
									odpowiednio zwraca True, jeżeli plansza jest pełna i False jeżeli jest jeszcze jakieś puste pole
		- Game		->	Jako argument przyjmuje obiekt klasy Board
					Głównymi metodami są:
						- throw_token	     ->	na podstawie zadanej kolumny i tokenu przeszukuje planszę, żeby znaleźć najniższe możliwe wolne miejsce,
									w to miejsce wstawia token (zamienia 0 na podaną wcześniej liczbę 1 lub 2 , czyli token konkretnego gracza)
						- check_victory	     ->	pobiera token gracza (1 lub 2) i sprawdza czy ten wygrał, tzn czy udało mu się ustawić tokeny 4 po kolei
									za pomocą innych metod klasy Game przepisuje każdy rząd, kolumnę i przekątną jako ciąg znaków (string)
									później sprawdza czy wygrany ciąg 4 tokenów ('1111' lub '2222') zawiera się w którymś z nich
									metoda zwraca True gdy dany gracz wygrał, albo False gry nie ma jeszcze wygranej
		- Bot		->	Jako argument przyjmuje obiekt klasy Game
					Głównymi metodami są:
						- find_best_column   ->	szuka najlepszej kolumny na podstawie największego 'wyniku' (score)
									aby znaleźć odpowiednią kolumnę tworzony jest tymczasowy obiekt obecnej gry
									następnie do każdej kolumny 'wrzucany' jest token bota i obliczany jest wynik danego rzutu
									obliczanie działa na podstawie szukania odpowiedniej konfiguracji tokenów w każdym rzędzie, kolumnie i przekątnej (jak w metodzie check_victory klasy Game)
									potem każdy wynik rzędu, kolumny i przekątnej jest sumowany i na podstawie ostatecznej listy wyników (metoda final_score_list) jest wybierana ta kolumna z najwyższym wynikiem 
									metoda zwraca numer najlepszej dla bota kolumny
						- create_temp_game   ->	tworzy dokładną kopię obecnego obiektu Game za pomocą funkcji deepcopy z biblioteki copy
									jest ona używana w innych metodach klasy Bot, aby przy testowym rzucie nie była zmieniana główna plansza gry
		- Interface	->	Nie przyjmuje żadnych argumentów
					Głównymi metodami są:
						- main_game_interface->	odpowiada za główna komunikacje z użytkownikiem programu i jest filarem całęgo interfejsu, kieruje kiedy jaka metoda ma być uruchomiona
									najpierw pyta użytkownika czy ma być rozpoczęta nowa gra, czy zapisana, czy może wyświetlić listę 10 najlepszych wyników (metoda show_scores)
									następnie pyta czy użytkownik chce zmienić rozmier planszy (jeżeli nie ustawiana jest domyślna) i tworzy obiekt klasy Game
									dalej pyta o tryb gry i wywołuje zależnie metody play_with_player albo play_with_bot
									na końcu po wygranej grze wywołuje metodę save_final_score
						- main_board_create  ->	jest wywoływana kiedy użytkownik chce sam ustawić wymiary planszy
									użytkownik ma wpisać liczbę całkowitą od 4 do 9 w wypadku wyjątku informuje o tym użytkownika i ponownie proszony jest o wpisanie poprawnych danych
									następnie dzięki podanym danym tworzony jest obiekt klasy Board i przekazywany jest dalej
						- show_scores	     -> pokazuje użytkownikowi w interfejsie tekstowym 10 najlepszych wyników zapisanych w pliku ('best_scores')
									każdy wyświetlony wynik wygląda według schematu:
										"{aktualna pozycja wyniku}.{zapisana nazwa gracza} won in {liczba tur} moves against other player (albo 'against bot' zależnie od trybu tamtej gry)."
						- play_with_player   ->	główna metoda trybu gracz vs gracz
									gra toczy się w pętli do czasu, aż któryś z graczy zwycięży
									po każdym ruchu gracza sprawdzane jest to czy użytkownik chce zapisać grę, jeżeli tak wywoływana jest funkcja save_game i program jest zatrzymywany
									sprawdzana jest także wygrana, albo to czy plansza jest pełna i wyświetlane są odpowiednie komunikaty
						- play_with_bot	     ->	główna metoda trybu gracz vs bot
									podobnie do metody play_with_player ale zamiast 2 gracza następuje ruch bota poprzez wybór kolumny metodą klasy bot (find_best_column) i wrzuceniu tokenu do tej kolumny
						- player_move	     ->	metoda ruchu każdego gracza
									ruch toczy się w pętli i sprawdza czy podana kolumna ma prawidłową wartość lub czy podana kolumna nie jest już pełna
									jeżeli jest odpowiednią liczbą całkowitą i kolumna ma miejsce to pętla jest stopowana i ruch gracza dobiega końca
						- print_gameboard    ->	pokazuje użytkownikowi w interfejsie tekstowym aktualny stan planszy za pomocą funkcji print dla każdego rzędu oraz pod planszą podpisuje numery kolumn
						- save_final_score   ->	pyta czy użytkownik chce zapisać swój wynik i jeżeli tak to prosi o podanie nazwy gracza
									dalej przekazuje argumenty odpowiednio do funkcji save_score_player albo save_score_bot (zależnie od wybranego trybu gry)
	2. Input/Output:
		
		(*Wszystkie pliki zapisywane są w postaci json)
		
		- save_game	-> 	zapisuje w pliku 'saved_game' odpowiednie dane gry w postaci słownika:
							- aktualna plansza gry 	('gameboard')
							- tryb gry 		('bot') (jeżeli gracz vs bot to True, jeżeli gracz vs gracz to False)
							- ostatni gracz 	('last_player')
							- aktualna tura 	('tour')
		- load_game	->	odczytuje z pliku zapisaną grę i zwraca krotkę kolejnych danych gry (kolejność zapisu)
					jeżeli pliku nie ma, nie ma do niego dostępu lub jest pusty to podnoszony jest wyjątek informujący o braku prawidłowego pliku zapisanej gry
		- save_score	->	jeżeli plik jest pusty albo go nie ma po prostu zapisywanu jest wynik w postaci słownika
							- nazwa gracza 		('name')
							- liczba tur 		('number of tours')
							- tryb gry		('played with bot')
					jeżeli były już jakieś wyniki to są odczytywane, potem sortowane po ilości tur (rosnąco) i zapisywane spowrotem do pliku
		- load_scores	->	wczytywane są wszystkie wyniki z pliku 'best_scores', a następnie sprawdzana jest długość listy
					jeżeli jest dłuższa od 10 to jest skracana do 10, aby przy wyświetlaniu wyników w interfejsie zachować przejrzystość

	3. Wyjątki:
		
		- WrongBoardDimensionsValueError	-> zostały źle podane wartości wysokości i szerokości podczas tworzenia planszy
		- FullColumnError			-> kolumna, do której użytkownik chce wrzucić token jest pełna
		- ColumnOutOfRangeError			-> kolumna, którą wybrał użytkownik ma za dużą lub za małą wartość
		- NoIntColumnError			-> kolumna, którą wybrał użytkownik nie jest liczbą całkowitą
		- WrongSaveGameFileError		-> nie ma odpowiedniego pliku zapisanej gry
		- WrongBestScoresFileError		-> nie ma odpowiedniego pliku najlepszych wyników
		- EmptyBestScoresFileError		-> plik z najlepszymi wynikami jest pusty



































