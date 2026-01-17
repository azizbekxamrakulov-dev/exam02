def filter_positive(numbers):
    result = []

    for element in numbers:
        if element["value"] > 0:
            result.append(element)

    return result


print(filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}]))
print(filter_positive([{'value': 0}, {'value': 5}, {'value': -3}]))