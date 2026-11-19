class DataProduct:
    """Store details about a data product."""

    def __init__(self, product_id, name, classification):
        """Set the product_id, name and classification for a product.

        Returns None.
        """
        self.product_id = product_id
        self.name = name
        self.classification = classification 

    def is_confidentiality(self):
        """Return True if the product is Confidential or Highly Confidential."""
        if self.classification == "Highly Confidential" or self.classification == "Confidential":
            return True
        return False


class AccessSubscription:
    """Store an access request for a data product."""

    def __init__(self, user_name, product_name, reason):
        """Set the user_name, product_name and reason for a pending request.

        Returns None.
        """
        self.user_name = user_name
        self.product_name = product_name
        self.reason = reason
        self.status = "Pending"

    def approve(self):
        """Set the subscription status to Approved and return None."""
        self.status = "Approved"


class MarketPlace:
    """Store products and access requests."""

    def __init__(self):
        """Create an empty marketplace and return None."""
        self.data_products = []
        self.access_subscriptions = []

    def add_data_product(self, data_product):
        """Add the given data_product to the marketplace and return None."""
        self.data_products.append(data_product)

    def request_access(self, user_name, product, reason):
        """Request access for user_name to a product, giving a reason.

        Return the new subscription. Confidential products stay pending;
        other products are approved.
        """
        new_subscription = AccessSubscription(user_name, product.name, reason)

        if not product.is_confidentiality():
            new_subscription.approve()

        self.access_subscriptions.append(new_subscription)
        return new_subscription