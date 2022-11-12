from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Post, Tag, Category, Comments
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    save_on_top = True
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('category', 'tags',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'author', 'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{ obj.photo.url }" width="50">')
        return '-'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'title')
    readonly_fields = ('user_name', 'user_email')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comments, CommentsAdmin)
