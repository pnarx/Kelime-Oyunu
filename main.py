
import random, string
from datetime import datetime
from itertools import count

dosya = open("zemberek.txt","r",encoding="utf-8")
def pick_random_word():
       word_list = [    "oku =dosya.read()"]
       random_word = random.choice(dosya.readlines())
       return random_word



def make_word_classified(word):
    classified_list = ["_" for i in word]
    return classified_list


def guess():
    word = pick_random_word()
    classified_word = make_word_classified(word)
    print(*classified_word)
    total_attempts = 0

    while True:
        try:
            answer = input("Bir harf tahmin et (Sadece bir harf yaz)>:").lower()

            if len(answer) > 1:
                raise Exception
            else:
                print("Girilen harf yok tekrar dene")
        except Exception:



            continue
        total_attempts += 1


        if total_attempts >= 15:
            print("Üzgünüm ama kaybettin!")
            try_again = input("Tekrar oynamak ister misin? (e veya h yazın) >: ")
            if try_again == 'e':
                guess()
            elif try_again == 'h':
                print("Yine bekleriz..")
                quit()

        for i in range(len(word)):
                if answer == word[i]:
                    classified_word[i] = answer
                if "".join(classified_word) == word:
                    print("Tebrikler kazandınn!")

                    quit()


        # if try_again == True:
        #        puan=0
         #       puan = count(try_again) * 5
          #      print("puanınız", puan)
        #if  count(try_again) == False:
        #        puan=0
         #       puan = puan - 3
          #      print("puanınız", puan)

        print(*classified_word, f"\nToplam kalan deneme: {15 - total_attempts}")


guess()