import bluetooth

nearby_devices = bluetooth.discover_devices(duration = 8, lookup_names = True, flush_cache=True, lookup_class = False)

print(nearby_devices)
#for addr, name in nearby_devices:
 #       print("hi")
  #      print("   {} - {}".format(addr,name)
    #except UnicodeEncodeError:
     #         print("   {} - {}".format(addr,name.encode("utf-8","replace")))
