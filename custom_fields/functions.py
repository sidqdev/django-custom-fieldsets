def setting_display_field(admin_order_field: str, boolean: bool = False, short_description: str = None):
    def wrap(func):
        func.boolean = boolean
        func.admin_order_field = admin_order_field
        if short_description is not None:
            func.short_description = short_description
        return func

    return wrap