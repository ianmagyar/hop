import random


def satisfies(setting):
    x1, x2, x3, x4, x5 = setting
    c1 = not x1 or not x2
    c2 = not x1 or not x3
    c3 = not x2 or not x3
    c4 = not x4
    c5 = not x4 or not x5
    c6 = x4 or x2 or not x3
    c7 = not x1 or not x4

    result = [c1, c2, c3, c4, c5, c6, c7]

    return all(result), result


def test_alternative(setting, change_id):
    _, original_results = satisfies(setting)
    original = sum(original_results)
    new_setting = setting.copy()
    new_setting[change_id] = not new_setting[change_id]

    _, new_result = satisfies(new_setting)
    new = sum(new_result)

    return new_result, new - original


def inner_loop(length, setting):
    for j in range(length):
        print("J={}".format(j + 1))
        print("The original setting is ", setting)
        sat, original = satisfies(setting)
        if sat:
            print(original)
            return setting

        changes = list()
        for elem_id, elem in enumerate(setting):
            total_meets, change = test_alternative(setting, elem_id)
            changes.append(change)

            print("Testing x{}, change {}".format(elem_id + 1, change))
            print(total_meets)
            print('-------')

        max_change = max(changes)
        candidates = list()
        for i in range(len(changes)):
            if changes[i] == max_change:
                candidates.append(i)

        print("Best changes: ", candidates)

        change_elem = random.choice(candidates)
        print("Changing x{}".format(change_elem + 1))

        setting[change_elem] = not setting[change_elem]

    return None


def gsat(i, j):
    for i_count in range(i):
        print("I={}".format(i_count + 1))
        start_setting = [random.choice([True, False]) for _ in range(5)]
        res = inner_loop(j, start_setting)

        if res:
            print("The solution is: ", res)
            return res

    return None


# sample = [False, False, True, False, True]
# found = inner_loop(2, sample)
# if found:
#     print("Solution: ", found)

gsat(10, 10)
