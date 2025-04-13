import random
import string
import sys

def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║  ███████╗████████╗██████╗  ██████╗ ███╗   ██╗ ██████╗       ║
    ║  ██╔════╝╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║██╔════╝       ║
    ║  ███████╗   ██║   ██████╔╝██║   ██║██╔██╗ ██║██║  ███╗      ║
    ║  ╚════██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║██║   ██║      ║
    ║  ███████║   ██║   ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝      ║
    ║  ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝       ║
    ║                                                              ║
    ║   🔒 PASSWORD GENERATOR 🔒    [ Secure • Random • Strong ]   ║
    ║                                                              ║
    ║          ╭─────────────────────────────────────╮            ║
    ║          │    Crafted with ❤️  by nahiirox     │            ║
    ║          ╰─────────────────────────────────────╯            ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def generate_password(length, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    # Define character sets
    uppercase = string.ascii_uppercase if use_uppercase else ''
    lowercase = string.ascii_lowercase if use_lowercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_symbols else ''
    
    # Combine selected character sets
    all_characters = uppercase + lowercase + numbers + symbols
    
    if not all_characters:
        return "Error: At least one character type must be selected"
    
    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # Ensure at least one character of each selected type is included
    required_chars = []
    if use_uppercase:
        required_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        required_chars.append(random.choice(string.ascii_lowercase))
    if use_numbers:
        required_chars.append(random.choice(string.digits))
    if use_symbols:
        required_chars.append(random.choice(symbols))
    
    # Replace first few characters with required ones
    password_list = list(password)
    for i, char in enumerate(required_chars):
        password_list[i] = char
    # Shuffle to make it more random
    random.shuffle(password_list)
    
    return ''.join(password_list)

def main():
    print_banner()
    print("\n" + "═" * 45)
    
    try:
        length = int(input("\n  Enter password length (1-60): "))
        if length <= 0:
            print("\n  ❌ Length must be positive")
            return
        if length > 60:
            print("\n  ❌ Maximum length is 60 characters")
            return
    except ValueError:
        print("\n  ❌ Please enter a valid number")
        return
    
    print("\n" + "═" * 45)
    print("\n  Select character types:")
    print("  1. Only numbers")
    print("  2. Numbers and lowercase letters")
    print("  3. Numbers and uppercase letters")
    print("  4. Numbers and both cases letters")
    print("  5. Numbers, lowercase letters, and symbols")
    print("  6. Numbers, uppercase letters, and symbols")
    print("  7. Everything (numbers, both cases, and symbols)")
    print("\n" + "═" * 45)
    
    try:
        choice = int(input("\n  Enter your choice (1-7): "))
        
        if choice == 1:
            password = generate_password(length, 
                use_uppercase=False, 
                use_lowercase=False, 
                use_symbols=False)
        elif choice == 2:
            password = generate_password(length, 
                use_uppercase=False, 
                use_symbols=False)
        elif choice == 3:
            password = generate_password(length, 
                use_lowercase=False, 
                use_symbols=False)
        elif choice == 4:
            password = generate_password(length, 
                use_symbols=False)
        elif choice == 5:
            password = generate_password(length, 
                use_uppercase=False)
        elif choice == 6:
            password = generate_password(length, 
                use_lowercase=False)
        elif choice == 7:
            password = generate_password(length)
        else:
            print("\n  ❌ Invalid choice")
            return
            
        print("\n" + "═" * 45)
        print(f"\n  🔐 Generated Password: {password}")
        print(f"  📏 Password length: {len(password)}")
        print("\n" + "═" * 45 + "\n")
        
    except ValueError:
        print("\n  ❌ Please enter a valid choice")

if __name__ == "__main__":
    main()
