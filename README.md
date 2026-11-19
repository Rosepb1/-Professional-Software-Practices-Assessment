# Data Marketplace

This prototype lets users request access to data products themselves. It checks
the data classification to decide if a request needs approval.

## Classes

- `DataProduct` stores a product's ID, name and classification.
- `AccessSubscription` stores an access request and its status.
- `MarketPlace` stores products and handles access requests.

## Getting started

With Python installed, run this code from the project folder:

```python
from MarketPlace import DataProduct, MarketPlace

marketplace = MarketPlace()
product = DataProduct(1, "Customer data", "Confidential")
marketplace.add_data_product(product)

request = marketplace.request_access("Alex", product, "Reporting")
print(request.status)  # Pending
```

## Data classification

Requests for `"Confidential"` and `"Highly Confidential"` products stay
`"Pending"` so they can be reviewed and approved. Requests for other
classifications are automatically marked `"Approved"`. The classification
names are case-sensitive.

This is a simple prototype: it records approval status but does not control
access to data or check who can approve a request.
