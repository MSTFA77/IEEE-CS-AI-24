def r(file):
    with open(file, 'r') as file:
        file_content = file.read()
        print("File content:")
        print(file_content)
def c(f):
    wc = {}
    with open(f, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.strip('.,!?;:').lower()
                if word:
                    wc[word] = wc.get(word, 0) + 1
    return wc
ftest = input("Enter the name of the text file: ")
r(ftest)
try:
        wc = c(ftest)
        print("Word counts:")
        for word, count in wc.items():
            print(f"{word}: {count}")
except FileNotFoundError:
        print("Error: File not found.")

