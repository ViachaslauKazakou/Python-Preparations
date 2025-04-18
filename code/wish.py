def wish():
    has_star = False
    user_input = ""
    while user_input != 'все!':
        user_input = input("Proceed: ").lower()
        if 'звезд' in user_input:
            has_star = True
            
    print("Hello, make a wish" if has_star else "No stars fall")

if __name__ == "__main__":
    wish()