from flume import Flume

flume = Flume()

supplier = flume.supplier.retrieve("001db284-9ab8-4504-90df-8d24196b5f53")

print(supplier)

item = flume.item.retrieve("aa090f33-1432-40cf-9b0c-ca5df2948489")
print(item)


customer = flume.customer.retrieve(item.customer_id)

print(customer)
