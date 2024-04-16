# from package.user import User

# package = __import__("12-package.user")

import importlib
# user = importlib.import_module('12-package.user')
package = importlib.import_module('12-package')

print(package.maktab_id)
# print(user.User)
# print(package.user.User)
# print(User)
