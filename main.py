from data import constant_numbers, room_data
from display import display_costs


def calculate_cost_profit(unit, num_days):
    cleaning_cost = constant_numbers["unit_cleaning_cost"]
    cost_profit_data = {}
    if unit == "A":
        cost_profit_data = calculate_oppotunity_cost(["AB"], num_days)
    elif unit == "B":
        cost_profit_data = calculate_oppotunity_cost(["AB"], num_days)
    elif unit == "AB":
        cleaning_cost *= 2
        cost_profit_data = calculate_oppotunity_cost(["A", "B"], num_days)
    opportunity_cost = cost_profit_data["total-opp-cost"]
    cleaning_fee = room_data[unit]["cleaning_fee"]
    service_cost = constant_numbers["service_cost"]
    cost_profit_data["service_cost"] = service_cost
    service_fee = room_data[unit]["service_fee"]
    mortgage_per_day = constant_numbers["mortgage_per_day"]

    cost_profit_data["mortgage_per_day"] = mortgage_per_day
    cost_profit_data['nightly-price'] = room_data[unit]["avg-nightly-price"]
    cost_profit_data[
        "total-cost-to-host"] = service_cost + cleaning_cost + opportunity_cost + mortgage_per_day - cleaning_fee - service_fee
    cost_profit_data["revenue"] = num_days * room_data[unit]["avg-nightly-price"]
    base_profit = cost_profit_data["revenue"] - cost_profit_data["total-cost-to-host"]
    net_profit = base_profit * (1 - constant_numbers["airbnb_cut"])
    cost_profit_data["profit"] = net_profit
    cost_profit_data["cleaning_fee"] = cleaning_fee
    cost_profit_data["service_cost"]
    return cost_profit_data


def calculate_oppotunity_cost(rooms, nights):
    costs = {"Nights": nights, "rooms": {}}
    total_cost = 0
    for room in rooms:
        nightly_price = room_data[room]["avg-nightly-price"]
        probability_of_booking = room_data[room]["occupancy-rate"]
        opp_cost = nightly_price * probability_of_booking * nights
        total_cost += opp_cost
        costs["rooms"][room] = {"Nightly price": nightly_price, "Probability of booking": probability_of_booking,
                                "Opportunity cost": opp_cost}
    costs["total-opp-cost"] = total_cost
    return costs


if __name__ == "__main__":
    display_costs(calculate_cost_profit("AB", 7))
    # display_costs(calculate_cost_profit("AB", 5))
    # display_costs(calculate_cost_profit("B", 10))
    # display_costs(calculate_cost_profit("A", 3))