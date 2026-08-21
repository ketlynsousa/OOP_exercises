from challenges.challenge011.employee import HourlyWorker, MonthlyWorker


def main():
    f1 = HourlyWorker('Paul', 12, 200)
    f1.salary_calculation()
    f1.salary_analyze()

    f2 = MonthlyWorker('Amanda', 9500)
    f2.salary_calculation()
    f2.salary_analyze()

if __name__ == '__main__':
    main()
