def solution(cacheSize, cities):
    total_time = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city_name = city.lower()
        

        if city_name in cache:
            total_time += 1
            
            cache.remove(city_name)
            cache.append(city_name)
            
        else:
            total_time += 5
            
            if len(cache) == cacheSize:
                cache.pop(0)

            cache.append(city_name)

    return total_time