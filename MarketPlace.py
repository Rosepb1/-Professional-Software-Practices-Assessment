class DataProduct:
    def __init__(self, product_id, name, classification):
        self.product_id = product_id
        self.name = name
        self.classification = classification 

    def is_confidentiality(self):
        if self.classification == "Highly Confidential" or self.classification == "Confidential":
            return True
        return False


class AccessSubscription:
    def __init__(self, user_name, product_name, reason):
        self.user_name = user_name
        self.product_name = product_name
        self.reason = reason
        self.status = "Pending"

    def approve(self):
        self.status = "Approved"


class MarketPlace:
    def __init__(self):
        self.data_products = []
        self.access_subscriptions = []

    def add_data_product(self, data_product):
        self.data_products.append(data_product)

    def request_access(self, user_name, product, reason):
        new_subscription = AccessSubscription(user_name, product.name, reason)

        if not product.is_confidentiality():
            new_subscription.approve()

        self.access_subscriptions.append(new_subscription)
        return new_subscription