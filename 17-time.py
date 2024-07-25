import time

# sleep: Suspend execution for n second
# print("Salam")
# time.sleep(1)
# print("Bye Bye")

# print(time.time())  # Unix Time, Epoch, 1/1/1970

# start_time = time.time()
# for _ in range(10 ** 8):
#     pass
# print("Execution Time:", time.time() - start_time)

# start_time = time.perf_counter()
# for _ in range(10 ** 8):
#     pass
# print("Execution Time:", time.perf_counter() - start_time)

# print("Epoch (Unix):", time.time())
# print("Localize:", time.ctime())
# print("Struct:", time.localtime())

# struct_time = time.localtime()
# print(struct_time.tm_hour)
# print("My Time:", time.strftime("%H:%M:%S", struct_time))
# print(time.strptime("16:15:05", "%H:%M:%S"))
