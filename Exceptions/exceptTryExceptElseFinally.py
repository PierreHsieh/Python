# coding:utf-8

# try => except => finally
# try => else => finally
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
