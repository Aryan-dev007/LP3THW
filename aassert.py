def apply_discount(product, discount):
    price = int(product * (1 - discount))
    assert 0 <= price <= product, "idk"
    return price


def react(num1, num2):
    sum = 0
    sum = num1+num2
    print(sum - 1)
    assert num1 <= num2, 'check config'


def gaali(hello, mello):
   #  gandu = (why,"ruko zara sabar kro")
    if not hello == mello:
        raise "same number daal."


gaali(23, 23)

react(3, 4)

apply_discount(50, 30)
