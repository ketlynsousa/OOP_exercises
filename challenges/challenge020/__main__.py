from challenges.challenge020.file import DOC, PDF, open_file


def main():
    a1 = DOC('exam', 850_000)
    a2 = PDF('contract', 1_200_000)


    open_file(a1)
    open_file(a2)

    print(f' - {a2.full_name}')

if __name__ == '__main__':
    main()
