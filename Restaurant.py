class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        print("Error: Cannot change restaurant name.")

    # Object Relationship Methods
def add_review(self, review):
        self._reviews.append(review)

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
        return total_ratings / len(self._reviews)