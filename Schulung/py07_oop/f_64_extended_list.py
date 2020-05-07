class elist(list):
    def flatten(self):
        result = elist([])
        for el in self:
            if type(el).__name__ == 'elist':
                result.extend(el.flatten())
            else:
                result.append(el)
        return result
            

if __name__ == '__main__':
    x = elist([elist([3,7]),4,6])
    print(x)
    x = x.flatten()
    print(x)
    x = ( elist([elist([3,7]),4,elist([6,elist([42,43])])]) )
    print(x[2])
    print(x.flatten())