# Task 1: Flight Route Comparison
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

# Print destinations that both airlines fly to
print(f"Destinations that both airlines fly to: {", ".join(our_routes.intersection(competitor_routes))}")

# Print destinations unique to our airline
print(f"Destinations that are unique to our airline: {", ".join(our_routes.difference(competitor_routes))}")

# Print whether there are any destinations that neither airline shares
if our_routes.symmetric_difference(competitor_routes):
    print(f"Destinations that neither airline shares: {", ".join(our_routes.symmetric_difference(competitor_routes))}")
else:
    print("There are no destinations that neither airline shares")