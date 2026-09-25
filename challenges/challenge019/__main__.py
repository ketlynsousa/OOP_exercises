from challenges.challenge019.employee import Manager, Designer, Developer


def main():

    #e = Manager('Peter', 8_000)
    #e.salary = 10_000
    #print(e)

    employees = [
        Developer('Peter', 18_000), Designer('Joseph', 25_000), Manager('Mary', 45_000)
    ]

    for e in employees:
        print(f' - {e}')


if __name__ == '__main__':
    main()
