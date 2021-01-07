def remove_ads_restaurants(restaurants):
    list_without_ads = []
    for restaurant in restaurants:
        if not restaurant['isPremium']:
            list_without_ads.append(restaurant)

    return list_without_ads