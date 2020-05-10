def return_underlying_security(current_price, price_before):
    return (current_price / price_before) - 1


def weight_price(prices, weight):
    return (weight / 100) * return_underlying_security(prices["current"], prices["before"])


# prices_with_weight = [{current: 1, before: 1, weight:10}, ]
def return_of_index(prices_with_weight):
    result = 0
    for price in prices_with_weight:
        result += weight_price({"current": price["current"],
                                "before": price["before"]}, price["weight"])
    return result


def price_of_index(index_price_before, securities_prices_weight):
    return index_price_before * (1 + return_of_index(securities_prices_weight))
