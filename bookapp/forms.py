from logging import PlaceHolder
from django.forms import ModelForm
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "status", "checked"]
        labels ={
            "checked": "Checked out by"
        }

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # field.widget.attrs.update({"class": "form"})
            self.fields["title"].widget.attrs.update({"class": "form-input", "placeholder": "Title"})
            self.fields["author"].widget.attrs.update({"class": "form-input", "placeholder": "Author"})
            self.fields["status"].widget.attrs.update({"class": "form-select"})
            self.fields["checked"].widget.attrs.update({"class": "form-select"})


            

