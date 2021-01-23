def printing(missing_people):
    print(len(missing_people))
    for p in missing_people:
        print(p)


def guests_filtration(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if guest[0].isdigit():
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    vip_guests = sorted(vip_guests)
    regular_guests = sorted(regular_guests)
    return vip_guests + regular_guests


def absent_people(guests, command):
    while True:
        guest_number = input()
        if guest_number == command:
            break
        guests.remove(guest_number)
    filtered_guests = guests_filtration(guests)
    return filtered_guests


def guest_list(n):
    guests = set()
    for _ in range(n):
        guests.add(input())
    return guests


n = int(input())
list_of_guests = guest_list(n)
missing_people_from_party = absent_people(list_of_guests, command="END")
printing(missing_people_from_party)