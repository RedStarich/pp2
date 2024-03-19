import json

with open('sample-data.json') as f:
    data = json.load(f)

imdata = data["imdata"]

phys = ["l1PhysIf"]

print("{:<50} {:<20} {:<8} {:<6}".format("DN", "Description", "Speed", "MTU"))
print("=" * 80)

for entry in imdata[:3]:
    for obj_name in phys:
        attr = entry[obj_name]["attributes"]
        print("{:<50} {:<20} {:<8} {:<6}".format(
            attr["dn"],
            attr.get("descr", ""),
            attr.get("speed", ""),
            attr.get("mtu", "")
        ))
        break
    