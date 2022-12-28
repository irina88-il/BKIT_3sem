def field(items, *args):
    
    assert len(args)>0
    if len(args) == 1:
        for i in items:
            a = i.get(args[0])
            if a != None:
                yield a
    else:
        for i in items:
            new_dict = {}
            for j in args:
                a = i.get(j)
                if a != None:
                    new_dict[j] = a
            yield new_dict    
  
    return 0

def main():
    goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}]
    a = field(goods, 'title','price')
    b = field(goods, 'title')
    for i in a:
        print(i, end = ' ')
    print('\n')
    for i in b:
        print(i, end = ' ')

if __name__ == "__main__":
    main()


            
        
        
    
    
