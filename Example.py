from MarketPlace import DataProduct, MarketPlace

marketplace = MarketPlace()

confidential = DataProduct("DP001", "Customer Data", "Confidential")
public = DataProduct("DP002", "Public Data", "Public")

marketplace.add_data_product(confidential)
marketplace.add_data_product(public)

confidential_request = marketplace.request_access(
    "Alex", confidential, "Monthly report"
)
public_request = marketplace.request_access(
    "Alex", public, "Public information"
)
highly_confidential = DataProduct("DP003", "Sensitive Data", "Highly Confidential")
marketplace.add_data_product(highly_confidential)

request = marketplace.request_access("Alex", highly_confidential, "Review")

print(f"Public request status: {public_request.status}")
print(f"Confidential request status: {confidential_request.status}")
print(f"Highly confidential request status: {request.status}")
