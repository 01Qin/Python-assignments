def numbers(integers_list):
    even_list = []
    for n in integers_list:
        if n % 2 == 0:
            even_list.append(n)
    return even_list


def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8]
    cut_down_list = numbers(original_list)
    print(f"original_list: {original_list}")
    print(f"cut_down_list: {cut_down_list}")
    return


main()
