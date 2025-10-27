Mynotebook={"name":"Hamdan Rugarama","campus": "kabale university", "city": "kasese", "language": "konzo", "religion": "Islam",
            "residence":"rwamukundi"}
print(Mynotebook["name"])
Mynotebook["residence"]="Hillside Hostels"
del Mynotebook["language"]
Mynotebook["sex"]="male"
for key, value in Mynotebook.items():
    print(f"{key}: {value}")
