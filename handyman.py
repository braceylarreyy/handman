class ServiceProvider:
    def __init__(self, name, profession, rating, hourly_rate):
        self.name = name
        self.profession = profession
        self.rating = rating
        self.hourly_rate = hourly_rate
        self.available = True

class Handyman:
    def __init__(self):
        self.service_providers = []

    def add_service_provider(self, provider):
        self.service_providers.append(provider)

    def find_providers(self, profession):
        return [provider for provider in self.service_providers if provider.profession.lower() == profession.lower() and provider.available]

    def book_provider(self, provider):
        if provider.available:
            provider.available = False
            return True
        return False

def main():
    app = Handyman()

    # Add some sample service providers
    app.add_service_provider(ServiceProvider("John Doe", "Mechanic", 4.5, 50))
    app.add_service_provider(ServiceProvider("Jane Smith", "Plumber", 4.8, 60))
    app.add_service_provider(ServiceProvider("Bob Johnson", "Cleaner", 4.2, 30))
    app.add_service_provider(ServiceProvider("Alice Brown", "Electrician", 4.7, 70))

    while True:
        print("\nWelcome to Handyman!")
        print("1. Find a service provider")
        print("2. Book a service provider")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            profession = input("Enter the type of service you need: ")
            providers = app.find_providers(profession)
            if providers:
                print(f"\nAvailable {profession}s:")
                for i, provider in enumerate(providers, 1):
                    print(f"{i}. {provider.name} - Rating: {provider.rating}, Hourly Rate: ${provider.hourly_rate}")
            else:
                print(f"No available {profession}s found.")

        elif choice == '2':
            profession = input("Enter the type of service you need: ")
            providers = app.find_providers(profession)
            if providers:
                print(f"\nAvailable {profession}s:")
                for i, provider in enumerate(providers, 1):
                    print(f"{i}. {provider.name} - Rating: {provider.rating}, Hourly Rate: ${provider.hourly_rate}")
                
                provider_index = int(input("Enter the number of the provider you want to book: ")) - 1
                if 0 <= provider_index < len(providers):
                    if app.book_provider(providers[provider_index]):
                        print(f"Successfully booked {providers[provider_index].name}!")
                    else:
                        print("This provider is no longer available.")
                else:
                    print("Invalid provider number.")
            else:
                print(f"No available {profession}s found.")

        elif choice == '3':
            print("Thank you for using Handyman. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()