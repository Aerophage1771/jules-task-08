import generate
generate.create_variant_1 = generate.make_variant1
generate.create_variant_2 = generate.make_variant2
generate.create_variant_3 = generate.make_variant3

with open("variant1.html", "w") as f:
    f.write(generate.make_variant1())
with open("variant2.html", "w") as f:
    f.write(generate.make_variant2())
with open("variant3.html", "w") as f:
    f.write(generate.make_variant3())

print("HTML files generated successfully.")
