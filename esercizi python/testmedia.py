"""
Testing manuale della funzione media.
"""


def media(numeri):
    return sum(numeri) / len(numeri)


def test_media():
    print("Test 1:", media([10, 20, 30]) == 20.0)
    print("Test 2:", media([1, 2, 3, 4]) == 2.5)
    print("Test 3:", media([5]) == 5.0)


if __name__ == "__main__":
    test_media()
