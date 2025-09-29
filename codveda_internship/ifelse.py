Measure_cost = float(input("\nEnter weight of product to determine cost of shipping.. \n"))

if  Measure_cost <= 1:
    print("Cost of shipping is :",  500,"frs")
elif Measure_cost <= 5:
     print("Cost of shipping is :",  1000,"frs")
else:
     print("Cost of shipping is ", 5000, "frs")


