import regions

region = regions.get_regions()

region.sort()

for i in region:
    print(i)