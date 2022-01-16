def dynamic_tabulation(step, _cache={}):
  if step in _cache:
    return _cache[step]
  elif step > 1:
    return _cache.setdefault(step, dynamic_tabulation(step - 1) + dynamic_tabulation(step - 2))
  return step
print(dynamic_tabulation(35))