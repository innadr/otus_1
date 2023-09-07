""" Считаем среднее арифметическое """

def calculate_average(input_nums):
    """
Функция подчета среднего арифметического
    :param input_nums:
    :return:
    """
    total = sum(input_nums)
    count = len(input_nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
