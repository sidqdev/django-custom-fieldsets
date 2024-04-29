from typing import List, Tuple


class CategoryLabel:
    def __init__(self, label: str, hidden: bool = False, hidden_for_superuser: bool = False, allowed_groups: List[str] = None) -> None:
        self.label = label
        self.hidden = hidden
        self.hidden_for_superuser = hidden_for_superuser
        self.allowed_groups = allowed_groups

    def __str__(self) -> str:
        return self.label
    
    def __repr__(self) -> str:
        return self.label
    
    def get_extra_fieldset_params(self, request):
        params = {}
        if self.hidden or (self.hidden_for_superuser and request.user.is_superuser):
            params.update({'classes': ('collapse', 'collapse-closed')})

        return params
    

class CategoryChoices:
    @classmethod
    def choices(cls) -> List[Tuple[str, CategoryLabel]]:
        values = list()
        for k, v in cls.__dict__.items():
            if isinstance(v, CategoryLabel):
                values.append((k, v))
        return values

    @classmethod
    def groups_to_access(cls, groups: list, is_superuser: bool):
        if is_superuser:
            return None
        
        categories = list()
        groups = set(groups)
        print(groups)
        for k, v in cls.choices():
            if v.allowed_groups is None or set(v.allowed_groups) & groups:
                categories.append(v)
        print(categories) 
        return list(set(categories))
