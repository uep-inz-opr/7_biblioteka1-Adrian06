class Biblioteka:

	lista_ksiazek = []
	lista_egzemplarzy = []
	final_list = []
	czy_w_liscie = False

	def __init__(self, limit_wypozyczen):
		self.limit_wypozyczen = limit_wypozyczen

	def sortuj(self, lst):
		return lst['tytul']

	def dostepne_egz(self):
		for ksiazka in self.lista_ksiazek:
			for egzemplarz in self.lista_egzemplarzy:
				if egzemplarz.tytul == ksiazka.tytul and egzemplarz.autor == ksiazka.autor:
					self.czy_w_liscie = True
			if  not self.czy_w_liscie:
					self.final_list.append({'tytul': ksiazka.tytul, 'autor': ksiazka.autor, 'ilosc_egzemplarzy': self.liczEgzemplarz(ksiazka)})
					self.czy_w_liscie = False
					self.lista_egzemplarzy.append(ksiazka)
			self.czy_w_liscie = False
		self.final_list.sort(key=self.sortuj)
		for lista in self.final_list:
			print("('" + lista['tytul'].strip() + "'" + ", " + "'" + lista['autor'].strip() + "', " + lista['ilosc_egzemplarzy'].strip() + ")")

	def liczEgzemplarz(self, aktualna_ksiazka):
		num = 0
		for ksiazka in self.lista_ksiazek:
			if aktualna_ksiazka.tytul == ksiazka.tytul and aktualna_ksiazka.autor == ksiazka.autor:
				num += 1
		return str(num)

	def dodaj_egzemplarz_ksiazki(self, ksiazka):
		self.lista_ksiazek.append(ksiazka)

class Ksiazka:
	def __init__(self, tytul, autor, rok_wydania):
		self.tytul = tytul
		self.autor = autor
		self.rok_wydania = rok_wydania

class Egzemplarz:
	def __init__(self, rok_wydania, wypozyczony):
		self.rok_wydania = rok_wydania
		self.wypozyczony = wypozyczony


ilosc_ksiazek = int(input())
lista_ksiazek = [input().strip(' ') for ksiazka in range(ilosc_ksiazek)]
usuwanie = []
biblioteka = Biblioteka(5)



for x in lista_ksiazek:
	usun_nawias = x.replace("(", "")
	usun_nawias2 = usun_nawias.replace(")", "")
	usun_cudzyslow = usun_nawias2.replace("\"", "")
	usuwanie = usun_cudzyslow.split(", ")
	ksiazka = Ksiazka(usuwanie[0], usuwanie[1], usuwanie[2])
	biblioteka.dodaj_egzemplarz_ksiazki(ksiazka)

biblioteka.dostepne_egz()