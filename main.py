# esercizio confronto tra metodo divisioni e moltiplicazioni
# verificare il numero di collisioni con i due metodi
from numpy import count_nonzero
from Hash_table import Hash_table
from random import randint
from statistics import mode


def main():
# a = n/m = 0.499
    a1 = Hash_table("m", 10013)      # tabella con metodo divisioni
    b1 = Hash_table("d", 10013)      # tabella con metodo moltiplicazioni
    for i in range(0, 5000):
        a1.insert(randint(0, 1000000))    # inserisco elementi in a e b
        b1.insert(randint(0, 1000000))
    print(a1.find(-8))

    sizes_a1 = []
    sizes_b1 = []

    for j in range(0, a1.get_size()):
        sizes_a1.append(a1.get_table()[j].size())     # vettori con dimensione delle liste di a e b
        sizes_b1.append(b1.get_table()[j].size())

    print("numero massimo di collisioni per a1: " + str(max(sizes_a1)) + "\n" + "numero massimo di collisioni per b1: " +
          str(max(sizes_b1)))       # massimo
    print("moda di collisioni per a1: " + str(mode(sizes_a1)) + "\n" + "moda di collisioni per b1: " + str(mode(sizes_a1)))  # moda
    print("celle con 0 elementi per a1: " + str(a1.get_size() - count_nonzero(sizes_a1)) + "\n" +
          "celle con 0 elementi per b1: " + str(b1.get_size() - count_nonzero(sizes_b1)))
    print("scarto massimo - minimo a1 : " + str(max(sizes_a1) - min(sizes_a1)) + "\n" +
           "scarto massimo - minimo b1 : " + str(max(sizes_b1) - min(sizes_b1)))

# a = n/m = 0.998
    a2 = Hash_table("m", 10013)      # tabella con metodo divisioni
    b2 = Hash_table("d", 10013)      # tabella con metodo moltiplicazioni
    for i in range(0, 10000):
        a2.insert(randint(0, 1000000))    # inserisco elementi in a e b
        b2.insert(randint(0, 1000000))
    print(a2.find(-8))

    sizes_a2 = []
    sizes_b2 = []

    for j in range(0, a2.get_size()):
        sizes_a2.append(a2.get_table()[j].size())     # vettori con dimensione delle liste di a e b
        sizes_b2.append(b2.get_table()[j].size())

    print("\nnumero massimo di collisioni per a2: " + str(max(sizes_a2)) + "\n" + "numero massimo di collisioni per b2: " +
          str(max(sizes_b2)))       # massimo
    print("moda di collisioni per a2: " + str(mode(sizes_a2)) + "\n" + "moda di collisioni per b2: " + str(mode(sizes_a2)))  # moda
    print("celle con 0 elementi per a2: " + str(a2.get_size() - count_nonzero(sizes_a2)) + "\n" +
          "celle con 0 elementi per b2: " + str(b2.get_size() - count_nonzero(sizes_b2)))
    print("scarto massimo - minimo a2: " + str(max(sizes_a2) - min(sizes_a2)) + "\n" +
           "scarto massimo - minimo b2: " + str(max(sizes_b2) - min(sizes_b2)))

# a = n/m = 1.997
    a3 = Hash_table("m", 10013)      # tabella con metodo divisioni
    b3 = Hash_table("d", 10013)      # tabella con metodo moltiplicazioni
    for i in range(0, 20000):
        a3.insert(randint(0, 1000000))    # inserisco elementi in a e b
        b3.insert(randint(0, 1000000))
    print(a3.find(-8))

    sizes_a3 = []
    sizes_b3 = []

    for j in range(0, a3.get_size()):
        sizes_a3.append(a3.get_table()[j].size())     # vettori con dimensione delle liste di a e b
        sizes_b3.append(b3.get_table()[j].size())

    print("\nnumero massimo di collisioni per a3: " + str(max(sizes_a3)) + "\n" + "numero massimo di collisioni per b3: " +
          str(max(sizes_b3)))       # massimo
    print("moda di collisioni per a3: " + str(mode(sizes_a3)) + "\n" + "moda di collisioni per b3: " + str(mode(sizes_a3)))  # moda
    print("celle con 0 elementi per a3: " + str(a3.get_size() - count_nonzero(sizes_a3)) + "\n" +
          "celle con 0 elementi per b3: " + str(b3.get_size() - count_nonzero(sizes_b3)))
    print("scarto massimo - minimo a3: " + str(max(sizes_a3) - min(sizes_a3)) + "\n" +
           "scarto massimo - minimo b3: " + str(max(sizes_b3) - min(sizes_b3)))


if __name__ == "__main__":
    main()
