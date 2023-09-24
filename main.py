def linearSearchProduct(productList,targetProduct):
  indices = []
  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
      
  return indices



products = ["shoes", "boot", "Loafer","shoes", "sandal","shoes","boot"]
target = "shoes"
target2="apple"
target3="boot"
result = linearSearchProduct(products, target3)
print(result)