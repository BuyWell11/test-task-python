import re


def prime_numbers(low, high):
    if not isinstance(low, int) or not isinstance(high, int) or low > high:
        return []
    primes = []
    for num in range(low, high+1):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


def text_stat(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except:
        return {'error': 'Ошибка чтения файла'}

    paragraphs = re.split(r'\n\s*\n', text)
    words = [re.findall(r'\w+', paragraph) for paragraph in paragraphs]

    # Частота использования каждой буквы алфавита
    letter_count = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    total_letters = sum(letter_count.values())
    letter_frequency = {letter: count /
                        total_letters for letter, count in letter_count.items()}

    # Количество слов в тексте
    word_amount = sum([len(paragraph) for paragraph in words])

    # Количество абзацев в тексте
    paragraph_amount = len(paragraphs)

    # Подсчет доли слов, в которых встречается конкретная буква
    letter_in_word_count = {}
    for word in [word.lower() for paragraph in words for word in paragraph]:
        for letter in set(word):
            letter_in_word_count[letter] = letter_in_word_count.get(
                letter, 0) + 1
    letter_proportion = {letter: letter_in_word_count[letter] / word_amount for letter in
                         letter_in_word_count.keys()}

    # Сбор всех частот связанных с буквами
    all_letter_stat = {}
    for letter, freq in letter_proportion.items():
        all_letter_stat[letter] = (letter_frequency[letter], freq)

    # Количества слов, в которых одновременно встречаются буквы обоих алфавитов
    bilingual_word_amount = sum(
        [1 for paragraph in words for word in paragraph if re.search(r'([а-яА-Я]+\w*[a-zA-Z]+\w*|[a-zA-Z]+\w*[а-яА-Я]+\w*)', word)])

    return {**all_letter_stat, 'word_amount': word_amount, 'paragraph_amount': paragraph_amount,
            'bilingual_word_amount': bilingual_word_amount}


def roman_numerals_to_int(roman_numeral):
    roman_values = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(roman_numeral)):
        if roman_numeral[i] not in roman_values:
            return None
        if i > 0 and roman_values[roman_numeral[i]] > roman_values[roman_numeral[i-1]]:
            result += roman_values[roman_numeral[i]] - \
                2 * roman_values[roman_numeral[i-1]]
        else:
            result += roman_values[roman_numeral[i]]
    return result
