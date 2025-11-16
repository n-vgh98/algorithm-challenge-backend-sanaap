from circle_pattern import build_lps
from longest_sub import longest_substring


def main():
    print("=== Task 1: Longest Unique Substring ===")
    s1 = input("Enter a string for longest unique substring: ")
    length = longest_substring(s1)
    print(f"Longest substring without repeating characters: {length}\n")

    print("=== Task 2: Circular Binary 1111 ===")
    s2 = input("Enter a binary string for circular 1111 check: ")
    print(f"Result a binary Circle is: {build_lps(s2)}")


if __name__ == '__main__':
    main()
