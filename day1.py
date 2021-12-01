import numpy as np


def a(input_file) -> int:
    """
    Finds the number of instances where a value in a file is bigger than the previous value

    :param input_file: file with number values, delimited by a new line
    :type input_file: str
    :return: sum of occasions where value increases
    :rtype: int
    """
    sonar_readings = np.loadtxt(input_file, delimiter="\n")

    sonar_diffs = np.diff(sonar_readings)
    return int(np.sum(sonar_diffs > 0))


def b(input_file, kernel_size=3) -> int:
    """
    Finds the number of instances where a rolling sum of values in a file is bigger than the previous rolling sum

    :param input_file: file with number values, delimited by a new line
    :type input_file: str
    :param kernel_size: size of rolling sum
    :type kernel_size: int
    :return: sum of occasions where value increases
    :rtype: int
    """
    sonar_readings = np.loadtxt(input_file, delimiter="\n")
    sonar_rolling_sum = np.convolve(sonar_readings,np.ones(kernel_size, dtype=int), 'valid')
    sonar_diffs = np.diff(sonar_rolling_sum)
    return int(np.sum(sonar_diffs > 0))


if __name__ == '__main__':
    ans1 = a("input/day1.txt")
    print("Day 1 Part a answer: ", ans1)

    ans2 = b("input/day1.txt")
    print("Day 1 Part b answer: ",ans2)
