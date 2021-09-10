from typing import List


def greet(first_name: str, last_name: str, titles: List[str], be_formal: bool) -> str:
    if be_formal:
        return 'How do you do, ' + ''.join(titles) + f' {last_name}?'
    return f'Hey, {first_name}'


print(greet('Tomás', 'Tamantini', ['Mr.'], False))

print(greet('Douglas', 'Vieira', ['Prof.', 'Dr.'], True))

'''
IDEs like PyCharm alert that the first and last name have the wrong type in the example below. But the code still runs
'''
print(greet(123, 321, [], False))
