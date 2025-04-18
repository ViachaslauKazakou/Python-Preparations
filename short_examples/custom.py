def custom(initial_count):
    print(f"Starting with {initial_count} cookies")
    for iteration in range(7):
        initial_count = max(round(initial_count / 2) + 1, 0)
        print(f"Remaining: {initial_count} after iteration {iteration}")
    return initial_count

if __name__ == "__main__":
    cookies = 0
    while True:
        remaining = custom(initial_count=cookies)
        print(f"Started with {cookies} cookies, ended with {remaining} cookies")
        
        if remaining == 2:
            print(f"We need {cookies} cookies at the start")
            break
        cookies += 1