print(f"\nDay 2: Iterables, Loops & Error Handling")
print(f"\nAssignment 1: Indexing Practice")

# List with 5 countries
countries = ["India", "USA", "Japan", "Canada", "Germany"]
print("\nCountries List Elements:")
print(countries[0])
print(countries[2])
print(countries[-1])

# Tuple with 4 programming languages
languages = ("Python", "Java", "React", "C++")
print("\nProgramming Languages Tuple:")
print(languages[0])
print(languages[3])

# String (your favorite quote)
quote = "In order to gain some thing we have to lose something."
print("\nQuote Characters:")
print(quote[0])     # First letter
print(quote[9])     # 10th character
print(quote[-1])    # Last character
print(quote[-2])
print(quote[4:9])  # Characters from index 4 to 8


print(f"\nAssignment 2: Even / Odd Filter")

ages = [18, 21, 25, 30, 42, 55, 60, 73]

print("\nEven Ages:")
for age in ages:
    if age % 2 == 0:
        print(age)

print("\nOdd Ages:")
for age in ages:
    if age % 2 != 0:
        print(age)

print(f"\nAssignment 3: Type Check with Error Handling")
data = [34, "Hot", 29.8, 41.2, "Rainy", 37.0]

for item in data:
    try:
        if type(item) == float:
            print(f"\nTemperature recorded: {item}°C")
        else:
            raise TypeError(f"Invalid entry: '{item}' is not a number")
    except Exception as err:
        print(f"\nError: {err}")

print(f"\nAssignment 4: API Monitor")

import requests

# Using free public API for testing
urls = [
    "http://35.184.187.16/app1/",
    "http://35.184.187.16/app2/",
    "http://35.184.187.16/app3/"
]

for url in urls:
    try:
        response = requests.get(url)
        print(f"\nChecking {url} - Status Code: {response.status_code}")

        if response.status_code == 200:
            print(" API Success:", response.json())
        else:
            print(" API Down or Invalid URL")

    except Exception as err:
        print(f" Network Error: {err}")

print(f"\nIf I have used differenr API it will be like this:")

import requests

# Using free public API for testing
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/users/3",
    "https://jsonplaceholder.typicode.com/invalid-url"
]

for url in urls:
    try:
        response = requests.get(url)
        print(f"\nChecking {url} - Status Code: {response.status_code}")

        if response.status_code == 200:
            print(" API Success:", response.json())
        else:
            print(" API Down or Invalid URL")

    except Exception as err:
        print(f" Network Error: {err}")
