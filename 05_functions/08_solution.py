def print_kwargs(**kwagrs):
    for key, value in kwagrs.items():
        yield value
        print(f"{key}:{value}")
        # print("\nPower ", power)


print_kwargs(power="Darshan", name="Money")
