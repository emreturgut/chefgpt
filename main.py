import subprocess

def main():
    print("Choose the AI chef personality to interact with:")
    print("1. Robot Chef")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        subprocess.run(["python3", "robot-chef.py"])

    else:
        print("Invalid choice. Please run the script again and choose a valid option.")

if __name__ == "__main__":
    main()