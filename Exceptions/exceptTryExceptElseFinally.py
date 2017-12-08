# coding:utf-8


try:
    raise NameError('Test')
    pass
except:
    print('catch an exception')
else:
    print('No Error')
finally:
    print('call finally')

# No Error
# call finally

# ======

# catch an exception
# call finally
