from django.db import models

def get_fieldset(
        model: models.Model, 
        categories: list = None, 
        categories_order: list = None,
        fieldsets: dict = None,
        request = None
    ):
    fieldsets = fieldsets or dict()
    categories_order = categories_order or list()

    for i in model._meta.get_fields():
        category = None
        try:
            category = i.category
        except:
            continue
        
        try:
            name: str = i.name
        except:
            continue
        
        if category in fieldsets:
            fieldsets[category].append(name)
        else:
            fieldsets[category] = [name]

    fieldsets_items = list(fieldsets.items())
    fieldsets_items.sort(
        key=lambda x: (
            categories_order.index(x[0])
            if x[0] in categories_order
            else len(fieldsets_items)
        )
    )

    return [
        (k, {"fields": v, **k.get_extra_fieldset_params(request)})
        for k, v in fieldsets_items if categories is None or k in categories
    ]


class ModelAdminMixin:
    extra_fieldsets = {}

    def get_fieldsets(self, request, obj=None):
        fieldset = dict((k, [x for x in v]) for k, v in self.extra_fieldsets.items())
        return get_fieldset(
            model=self.model, 
            fieldsets=fieldset, 
            categories_order=[x[1] for x in self.model.FieldCategory.choices()],
            categories=self.model.FieldCategory.groups_to_access(
                [x.name for x in request.user.groups.all()],
                request.user.is_superuser
            ),
            request=request
        )