def test_fn(*args):
    print(args)
    print(*args)
    
test_fn(2,3,4,5)


def order_pizza(*topings, **details): 
    print(f'New order arrived'
        #   f'for {size} pizza'
          f'with' )
    for i in topings:
        print(f'{i}')
    for i in details:
        print(details)

    
order_pizza("large", "mushroom", "olive", "pinapple", delivery=True, tip=5)