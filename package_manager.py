import time
import sys

def install_package(package_name):
    print(f"Installing {package_name}...")
    sys.stdout.write("[%s]" % (" " * 20))
    sys.stdout.flush()
    for i in range(21):
        time.sleep(0.1)  # Simulate installation time
        sys.stdout.write("\b" * 21)  # Move cursor back to the beginning of the progress bar
        sys.stdout.write("=" * i + ">" + " " * (20 - i))  # Print progress
        sys.stdout.flush()
    print("\nPackage installed successfully!")

def main():
    print("Welcome to the Python Package Manager!")
    print("Available packages:")
    packages = ["numpy", "matplotlib", "requests", "pandas"]  # Example list of packages
    for i, package in enumerate(packages, start=1):
        print(f"{i}. {package}")

    installed_packages = []
    while True:
        choice = input("Enter the number of the package you want to install (or 'q' to quit): ")
        if choice.lower() == 'q':
            break
        try:
            choice = int(choice)
            if choice < 1 or choice > len(packages):
                print("Invalid choice. Please enter a valid number.")
            else:
                package_name = packages[choice - 1]
                if package_name in installed_packages:
                    print(f"{package_name} is already installed.")
                else:
                    install_package(package_name)
                    installed_packages.append(package_name)
        except ValueError:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()
