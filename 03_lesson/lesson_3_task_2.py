from smartphone import Smartphone

catalog = [
    Smartphone("Nokia", "N_97", "89109101010"),
    Smartphone("Iphone", "Xr", "89209202020"),
    Smartphone("Samsung", "A_61", "89309303030"),
    Smartphone("Realmi", "C_61", "89409404040"),
    Smartphone("Xiaomi", "14", "89509505050")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} - {smartphone.number}")
