from pymonad import curry, State, unit


@curry
def buy_item(item_name, user):
    @State
    def state_computation(prev_state):
        if items.get(item_name) is None:
            print("item doesn't exist")
            return user, prev_state
        if user["money"] - items.get(item_name) < 0:
            print("Not enough money")
            return user, prev_state
        if item_name not in user["items"]:
            user["items"][item_name] = 1
        else:
            user["items"][item_name] += 1
        user["money"] -= items.get(item_name)
        return user, prev_state + items[item_name]

    return state_computation



user = {"items": {}, "money": 2000}

items = {
    "apples": 70,
    "wine": 300,
    "milk": 80,
    "chips": 100,
}


if __name__ == '__main__':


    user_init = unit(State, user) >> buy_item("apples") >> buy_item("wine") >> buy_item("apples") >> buy_item("foobar") >> \
    buy_item("wine") >> buy_item("chips")>> buy_item("chips")>> buy_item("chips")
    print(user_init(0))
