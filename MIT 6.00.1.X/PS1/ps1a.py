def count_vowels(s):
    vowels = 'aeiou'
    vowel_count = 0

    for letter in s:
        if letter in vowels:
            vowel_count += 1

    print("Number of vowels: ", vowel_count)


count_vowels('ixxzsbvgvgpea')
