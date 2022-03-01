import random
#ustalanie wielkości tablicy;
Number = 50
#List = [Number]
List = []
i = Number
print("Losujemy", Number, "liczb od 0 do 20:")
while i > 0:
    List.append(random.randint(0,20))
    print(List[Number-i])
    i -= 1
while i > 0:
    print(List[i])
    i -= 1
temp = 0
print("\nteraz wylosowane wczsniej liczby sortujemy :")
for i in range(1, Number):
    N = Number - 1
    while N > 0:
        #jeżeli chcemy listę rosnąco wtedy: "<", jeżeli chcemy malejąco: ">"
        if List[N] < List[N-1]:
            #zamiast tej operacji możemy użyć funkcji "re"
            temp = List[N]
            List[N] = List[N-1]
            List[N-1] = temp
        N -= 1
#wyświetlanie listy
for i in range(0,Number):
    print(List[i])