from AudioManager import *
from lpc_alg import get_formants
import numpy
from dtw_alg import dtw
from sklearn.metrics.pairwise import euclidean_distances
import warnings


if __name__ == '__main__':
    auto_treshold()
    while 1:
        print("Select an option:")
        option = input("\t[1] Learn\n\t[2] Search word\n\t[3] Search sentence\n\t[4] Exit\nCommand: ")
        name = ""

        if option == "1":
            name, user = record_to_file()
            sample = get_formants(name)
            with open("Base.txt", "a") as txt_file:
                txt_file.write(user)
                txt_file.write(" - ")
                txt_file.write(name)
                txt_file.write(" - ")
                numpy.savetxt(name + ".cff", sample)
                txt_file.write(name + ".cff")
                txt_file.write("\n")
        elif option == "2":
            record_to_file("Tmp.wav")
            print("Search...")
            word_1 = get_formants("Tmp.wav")
            counter = 0
            speaker = ""
            rec_word = ""
            found = 0
            with open("Base.txt", "r") as f:
                for line in f:
                    arr = line.split(" - ")
                    speaker = arr[0]
                    rec_word = arr[1]
                    word_2 = numpy.loadtxt(arr[2])
                    warnings.simplefilter("ignore")
                    distance = dtw(word_1, word_2, euclidean_distances)
                    if distance < 0.485:
                        found = 1
                        print("Word: ", rec_word)
                        print("Speaker: ", speaker)
                        print("Precision: ", (1 - 0.485 + distance) * 100, "%")
                    counter += 1
            if found == 0:
                print("No words found :[")
        elif option == "3":
            record_to_file("Tmp.wav")
            k = split("Tmp.wav")
            print("Search...")
            print(k)
            word_1 = get_formants("Tmp.wav")
            counter = 0
            speaker = ""
            rec_word = ""
            found = 0
            with open("Base.txt", "r") as f:
                for line in f:
                    arr = line.split(" - ")
                    speaker = arr[0]
                    rec_word = arr[1]
                    word_2 = numpy.loadtxt(arr[2])
                    warnings.simplefilter("ignore")
                    distance = dtw(word_1, word_2, euclidean_distances)
                    if distance < 0.485:
                        found = 1
                        print("Sentence: ", rec_word)
                        print("Speaker: ", speaker)
                        print("Precision: ", (1 - 0.485 + distance) * 100, "%")
                    counter += 1
            if found == 0:
                print("No sentence found :[")
        else:
            break
    print("Program exited successfully")
