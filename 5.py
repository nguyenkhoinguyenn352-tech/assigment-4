def even_only(lst):
    return [x for x in lst if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6]
print("Gốc:", nums)
print("Chẵn:", even_only(nums))
