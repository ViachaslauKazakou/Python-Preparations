
def custom(count):
    print(f"Have {count} cookies")
    for custom in range(7):
        count = (lambda x: round(x / 2) + 1 if x > 0 else 0)(count)
        print(f"rest: {count} after custom {custom}")
    return count

if __name__ == "__main__":
    cookies = 0
    while True:
        rest = custom(count=cookies)
        print(f"Customs get {cookies} and return {rest} cookies")
        
        if rest == 2:
            print(f"We need  {cookies} cookies on start")
            break
        else:
            cookies += 1