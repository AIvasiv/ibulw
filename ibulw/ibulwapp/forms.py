from django import forms
from .models import Expense_Items

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense_Items
        fields = ('category', 'amount', 'date', 'description')
        labels = {
            'category': 'Category',
            'amount': '$ Amount'
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        self.fields['description'].required = False