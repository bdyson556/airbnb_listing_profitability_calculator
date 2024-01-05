# TODO: incorporate Airbnb cut
# TODO: incorporate A AND B booking?
# TODO: incorporate maintenance costs

room_data = {
    "A": {
        "avg-nightly-price": 80,    # TODO: could specify weeknight vs weekend prices
        "occupancy-rate": 0.25,
    },
    "B": {
        "avg-nightly-price": 65,
        "occupancy-rate": 0.25,
    },
    "AB": {
        "avg-nightly-price": 110,
        # "avg-nightly-price": 94,
        "occupancy-rate": 0.50,
    }
}

unit_cleaning_fee = 40
service_fee = 5
mortgage_per_day = 1550 / 30

def calculate_cost_profit(unit, num_days):
    cleaning_fee = unit_cleaning_fee
    cost_profit_data = {}
    if unit == "A":
        cost_profit_data = calculate_oppotunity_cost(["AB"], num_days)
    elif unit == "B":
        cost_profit_data = calculate_oppotunity_cost(["AB"], num_days)
    elif unit == "AB":
        cleaning_fee *= 2
        cost_profit_data = calculate_oppotunity_cost(["A", "B"], num_days)
    opportunity_cost = cost_profit_data["total-opp-cost"]
    cost_profit_data['nightly-price'] = room_data[unit]["avg-nightly-price"]
    cost_profit_data["total-cost-to-host"] = service_fee + cleaning_fee + opportunity_cost + mortgage_per_day
    cost_profit_data["revenue"] = num_days * room_data[unit]["avg-nightly-price"]
    cost_profit_data["profit"] = cost_profit_data["revenue"] - cost_profit_data["total-cost-to-host"]
    return cost_profit_data

def calculate_oppotunity_cost(rooms, nights):
    costs = {"Nights": nights, "rooms": {}}
    total_cost = 0
    for room in rooms:
        nightly_price = room_data[room]["avg-nightly-price"]
        probability_of_booking = room_data[room]["occupancy-rate"]
        opp_cost = nightly_price * probability_of_booking * nights
        total_cost += opp_cost
        costs["rooms"][room] = {"Nightly price": nightly_price, "Probability of booking": probability_of_booking, "Opportunity cost": opp_cost}
    costs["total-opp-cost"] = total_cost
    return costs

def display_costs(data):
    print(data)

    print("=====")
    print(f"COSTS\t\t\t\t\t\t\t{data['total-cost-to-host']}")
    print("=====")
    print()
    print(f"Service charge:\t\t\t\t\t{service_fee}")
    print(f"Total opportunity cost:\t\t\t{data['total-opp-cost']}")
    for key, value in data['rooms'].items():
        print(f"\t\t\t{key}:\t{value}")
    print(f"Daily mortgage:\t\t\t\t\t{mortgage_per_day}")
    print(f"TOTAL COST:\t\t\t\t\t\t{data['total-cost-to-host']}")
    print(f"Cost per day:\t\t\t\t\t{data['total-cost-to-host'] / data['Nights']}")
    print()
    print("=====")
    print(f"REVENUE\t\t\t\t\t\t\t{data['revenue']}\t\t\t({data['Nights']} nights * ${data['nightly-price']})")
    print("=====")
    print()
    print("=====")
    print(f"PROFIT\t\t\t\t\t\t\t{data['profit']}")
    print("=====")

if __name__ == "__main__":
    display_costs(calculate_cost_profit("AB", 2))   # 2 nights to break even.
    # display_costs(calculate_cost_profit("AB", 5))
    # display_costs(calculate_cost_profit("B", 10))   # 10 nights to even BREAK EVEN!
    # display_costs(calculate_cost_profit("A", 4))   # 4 nights to break even!
