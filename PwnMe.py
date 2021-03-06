import argparse
import io
import itertools
import os
import time

try:
    os.system('cls')
    t0 = time.time()
    parser = argparse.ArgumentParser(description='A script to perform bruteforce dictionary attacks on brainwallets.')
    parser.add_argument('-p', action='store', dest='password',
                        help='Password that the script is guessing', required=True)
    parser.add_argument('-i', action='store', nargs='+', dest='info',
                        help='Relevant information that someone might have about you. ex: birthday dogs name childhood friend your name.\n'
                             'These should be separated by Spaces. ex: September 24 Spot Johnny Appleseed Jon Doe')
    args = parser.parse_args()
    print("This Script will attempt to guess the password you supply."
          "\nThis can be used to evaluate how easily your password can be 'pwnend'.")

    # Get number of passwords in wordlist
    dict_file = io.open("phpbb.txt", "r")
    num_words = 0
    for wordcount in dict_file:
        words = wordcount.splitlines()
        num_words += len(words)
    dict_file.close()
    # Guess password
    dict_file = io.open("phpbb.txt", "r")
    passCount = 0
    passFound = False
    for raw_word in dict_file:
        dictionary_word = raw_word.rstrip()
        words = raw_word.splitlines()
        passCount += len(words)
        print("[{} of {}]".format(passCount, num_words), end="\r")
        if dictionary_word == args.password:
            passFound = True
            os.system("cls")
            t1 = time.time()
            print("FOUND! Is your password {}?\nIt took {} seconds to guess your password.".format(dictionary_word, round(t1-t0, 2)))
            break
    dict_file.close()
    if not passFound and args.info != None:
        os.system("cls")
        print("Password not found using word list, trying info user provided.")
        time.sleep(1)
        userInfoList = []
        for i in range(len(args.info)):
            InfoList = list(itertools.product(args.info, repeat=i))
            userInfoList.append(InfoList)
        userInfoList = list(itertools.chain.from_iterable(userInfoList))
        for x in range(len(userInfoList)):
            if ''.join(userInfoList[x]) == args.password:
                os.system("cls")
                t1 = time.time()
                print("FOUND! Is your password {}?\nIt took {} seconds to guess your password.".format(''.join(userInfoList[x]), round(t1-t0, 2)))
                passFound = True
                break

    if not passFound and args.info is None:
            print("Password not found.\nTry adding relevent info that an attacker may know using the -i argument")
    elif not passFound:
        os.system("cls")
        print("Password could not be found. Good job.")
except KeyboardInterrupt:
    os.system("cls")
    print("You rage quit PwnMe!")



