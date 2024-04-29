## Custom fieldset settings for django admin with groups access

```python3
# models.py
import custom_fields

class Test(models.Model):
    class FieldCategory(custom_fields.CategoryChoices):
        category_a = custom_fields.CategoryLabel('category_a') # 1
        category_b = custom_fields.CategoryLabel(
            'category_b', 
            hidden_for_superuser=True
            allowed_groups=['Group names who can see and edit']
        ) 

    test_row_1 = custom_fields.CharField(max_length=40, category=FieldCategory.category_a)
    test_row_2 = custom_fields.CharField(max_length=40, category=FieldCategory.category_a)

    test_row_3 = custom_fields.CharField(max_length=40, category=FieldCategory.category_b)
    test_row_4 = custom_fields.CharField(max_length=40, category=FieldCategory.category_b)


# admin.py
import custom_fields

class TestAdmin(custom_fields.ModelAdminMixin, admin.ModelAdmin):
    readonly_fields = ("extra_field", )

    extra_fieldsets = {
        Test.FieldCategory.category_a: [
            "extra_field", # For extra fields outside of model
        ]
    } # optional

    def extra_field(self, obj: Test):
        return f"#{obj.id}"      
```

