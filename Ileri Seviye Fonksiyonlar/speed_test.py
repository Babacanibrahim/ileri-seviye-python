import time

def speed_test(fn):
    def inner(*args, **kwargs):
        start_time = time.time()
        print(f"{fn.__name__} fonksiyonu çalışıyor.")
        result = fn(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"Geçen süre {run_time}")
        return result
    return inner


@speed_test
def sum_gen():
    return sum((i for i in range(10000000)))

@speed_test
def sum_list():
    return sum([i for i in range(10000000)])

print(sum_gen())
print(sum_list())


# ÇIKTI

# sum_gen fonksiyonu çalışıyor.
# Geçen süre 0.6697287559509277
# 49999995000000

# sum_list fonksiyonu çalışıyor.
# Geçen süre 0.8049993515014648
# 49999995000000