from deta import Deta

# While using our SDKs(the latest versions) within a Deta Micro, you can omit
# specifying the project key when instantiating a service instance.
_deta = Deta(
    #'project key'
)


def get_users():
    # This how to connect to or create a database.
    # You can create as many as you want without additional charges.
    return _deta.Base('users')
