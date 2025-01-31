chai_types = {'Masala': ['Kadak', '200Ml'], 'Ginger' : ['Zesty', '100Ml'], 'Green' : ['Healthy', '100Ml']}
# print(chai_types)

for chai in chai_types:
    print(chai)
    print(chai, chai_types[chai])
    print(chai, chai_types[chai][1])
    
if "Masala" in chai_types:
    print("Available")

chai_types.pop("Masala")
chai_types.popitem()
    
chai_types["Black"] = ['No Milk', '60Ml']

print(chai_types)



tea_shop = {
    "chai" : {'Masala': ['Kadak', '200Ml'], 'Ginger' : ['Zesty', '100Ml'], 'Green' : ['Healthy', '100Ml']},
    "Cookie" : {'Wheat': [100, 'Chochlate'], 'Bun' : [25, 'Maska Bun']}
}

for pro in tea_shop:
    print(pro, tea_shop[pro])
    print()
    
# for key, value in chai_types.items():
#     print(key, value)