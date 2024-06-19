def anagram(s1,s2):

    if (sorted(s1)==sorted(s2)):
        print("It's an anagram")

    else:
        print("Not an anagram")

s1="listen"
s2="silent"

anagram(s1,s2)