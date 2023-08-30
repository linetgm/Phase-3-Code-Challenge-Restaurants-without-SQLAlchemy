class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []
        print(f"Created restaurant: {self._name}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        print("Error: Cannot change restaurant name.")

    # Object Relationship Methods
    def add_review(self, review):
        self._reviews.append(review)
        print(f"Added review for {self._name}")

    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    # Aggregate and Association Methods
    def average_star_rating(self):
        if len(self._reviews) == 0:
            return 0
        total_ratings = sum(review.rating() for review in self._reviews)
        avg_rating = total_ratings / len(self._reviews)
        print(f"Average star rating for {self._name}: {avg_rating}")
        return avg_rating


# Example usage
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")
restaurant1.add_review("Review A")
restaurant2.add_review("Review B")

print(restaurant1.name)
print(restaurant2.name)
restaurant1.name = "New Name"
print(restaurant1.name)
print(restaurant1.average_star_rating())
