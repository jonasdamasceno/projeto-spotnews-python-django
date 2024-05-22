from django import forms
from news.models import News, User, Category


class CreateCategoryForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        max_length=200,
        required=True,
    )


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["author"].label = "Autoria"
        self.fields["author"].widget = forms.Select(
            choices=[(user.id, user.name) for user in User.objects.all()]
        )
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["image"].label = "URL da Imagem"
        self.fields["categories"].widget = forms.CheckboxSelectMultiple()
        self.fields["categories"].label = "Categorias"
        self.fields["categories"].queryset = Category.objects.all()
