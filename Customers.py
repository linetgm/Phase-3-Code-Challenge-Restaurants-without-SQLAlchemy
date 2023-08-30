from Reviews import Review
from Restaurant import Restaurant
class Customer:

    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self.__class__.all_customers.append(self)
        self._reviews = []
        print(f"Created customer: {self.full_name()}")

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers

    # Object Relationship Methods
    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)
        print(f"Added review for {restaurant.name()} by {self.full_name()}")

    def restaurants(self):
        reviewed_restaurants = set()
        for review in self._reviews:
            reviewed_restaurants.add(review.restaurant())
        return list(reviewed_restaurants)

    # Aggregate and Association Methods
    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls.all_customers:
            if customer.full_name() == full_name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all_customers:
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers


# Example usage
customer1 = Customer("Linet", "Muthii")
customer2 = Customer("Joy", "Brittany")
rest1 = Restaurant("Kijiji")
customer1.add_review(rest1, 4)
# customer2.add_review("Restaurant B", 5)

print(Customer.find_by_name("Linet Muthii"))
print(Customer.find_all_by_given_name("Joy"))
print(customer1.given_name)

