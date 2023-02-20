from store_app.models import Store


def get_stores():
    """
    Get store addresses. This is used in CustomSignupForm to display available stores.
    :return: a tuple of available stores.
    """

    store_addresses = tuple((f"{store.store_id}", f"{store}") for store in Store.objects.all())

    return store_addresses
