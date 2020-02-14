import time

CACHE = {}

def queryOne(sql):
    try:
        result = CACHE[sql]
    except KeyError:
        time.sleep(1)
        result = 'execute %s' % sql
        CACHE[sql] = result
    return result

def queryTwo(sql):
    result = CACHE.get(sql)
    if not result:
        time.sleep(1)
        result = 'execute %s' % sql
        CACHE[sql] = result
    return result


if __name__ == '__main__':
    start = time.time()
    queryOne('SELECT * from blog_post')
    print(time.time()-start)

    start = time.time()
    queryOne('SELECT * from blog_post')
    print(time.time()-start)

    CACHE = {}
    start = time.time()
    queryTwo('SELECT * from blog_post')
    print(time.time()-start)

    start = time.time()
    queryTwo('SELECT * from blog_post')
    print(time.time()-start)

