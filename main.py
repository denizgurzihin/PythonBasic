import math
########################################################################################################################
# first question
print(" Question 1:")
array_1A = [67, 'ankara', 'istanbul', 20, 'izmir']
array_1B = ['izmir', 20, 'istanbul', 'ankara', 67]

print("First array is " + str(array_1A))
print("Second array is " + str(array_1B))

def question_1(arr1, arr2):
    length = len(arr1)          # ilk arrayin uzunluğunu bulduk
    length_2 = len(arr2)        # ikinci arrayin uzunluğunu bulduk

    if(length==length_2):       # iki arrayin uzunluğu eşit mi kontrol ettik
        for index in range(length):     #eşitse her elemanı tersindeki eleman ile eşitliğini kontrol ettik
            if(arr1[index] != arr2[length-index-1]):        #eğer eşit olmayan eleman bulursak false return ettik
                return False
        return True                     # eşitse True return etttik
    else:
        return False            # eşit değlse False return ettik

sol_1 = question_1(array_1A, array_1B)  # yazdığımız function çağırdık ve sonucu değişkene verdik
print("The result is " + str(sol_1))
print("-------------------------------------------------------------------------")


########################################################################################################################
# second question
print("\n Question 2:")
array_2 = [10, 20, 30, 40, 50, 60, 70]
print("The input array is " + str(array_2))

def question_2(arr1):
    new_arr = []                            # yeni bir array tanımladık
    length = len(arr1)                      # verdiğimiz input arrayin uzunluğunu bulduk
    length_half = math.floor(length/2)      # ve uzunluğuun yarısını bulup, en yakın en küçük sayıya yuvarladık 4.5sa 4 gibi
    length_control = length % 2             # length çiftse 0, tekse 1
    if(length_control==0):                  # eğer çift sayıda eleman varsa, farklı bir şekilde arraye yüjke
        for index in range(length):         # 0dan başla, arrayin son indexine kadar tekrarla
            if (index < length_half):       # indeximiz yarıdan azsa
                new_arr.append(arr1[length_half + index])       # arraydeki indexi, ortadaki index ve güncel index ile topla ve bunu yeni arraye yükle(append)
            if (index >= length_half):      # indeximiz yarıya eşit veya fazla ise
                new_arr.append(arr1[index - length_half])       #arraydeki indexi, şuanki indexden yarısının indexini çıkar, ve arraye yükle
    elif(length_control==1):                # eğer tek sayıda eleman varsa, farklı bir şekilde arraye yüjke
        for index in range(length):
            if (index < length_half):       #yukardaki gibi kontrol edip yükledik gene
                new_arr.append(arr1[ length_half + index + 1 ])
            elif(index == length_half):
                new_arr.append(arr1[length_half])
            elif(index > length_half):
                new_arr.append(arr1[ index - length_half - 1 ])
    return new_arr

sol_2 = question_2(array_2)
print("The result array is " + str(sol_2))
print("-------------------------------------------------------------------------")

########################################################################################################################
# third question
print("\n Question3:")
def question_3():
    n = input("Enter an Integer: ")

    while(len(n)!=1 or ord(n) < 49 or ord(n) > 57):                # aldığımız input, 1 ve 9 aralığında tek bir sayı mı diye kontrol edelim.
        print(n + " is not a valid input...")
        n = input("Enter an Integer: ")

    int_n = int(n)                                                 # kullanıcıdan aldığımız değeri integer değişkenine çeviriyoruz
    result = int_n + (11*int_n) + (111*int_n) + (1111*int_n) + int(11111*int_n)             # istenen formulü implemente edip, sonucu buluyoruz
    print(" When n is "+str(int_n)+", result of n + nn + nnn + nnnn + nnnnn is " + str(result))         #sonucu ekrana bastırıyoruz
    return result                                                   # bastırdığımız sonucu ayrıca bir değişkene return ediyoruz

sol_3 = question_3()
print("-------------------------------------------------------------------------")

########################################################################################################################
print("\n Question4: ")
def question_4():

    string = input("Enter an string: ")         # kullanıcıdan bir yazı istedik

    set_string = set(string)                    # bu yazıda geçen karakterleri bulduk
    dictionary = {}                             # karakterleri koymak için bi sözlük oluşturduk
    for elements in set_string:                 # bulduğumuz karakterler içinden, teker teker seçtkik
        number = string.count(elements)         # seçtiğimiz karakterin, inputta kaç defa geçtiğini bulduk
        dictionary[elements] = number           # bulduğumuz sonuçları sözlük yapısına ekledik

    print(dictionary)                           # sözlüğü ekrana bastırdık
    return dictionary                           # ayrıca sözlüğü, bir değişkene return yaptık

sol_4 = question_4()
print("-------------------------------------------------------------------------")