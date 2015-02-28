from django.contrib import admin
from myblog.models import Post, Category
from django.utils import timezone


def make_published(modeladmin, request, queryset):
    queryset.update(published_date=timezone.now())
make_published.short_description = 'Publish selected posts'


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline,)
    actions = (make_published,)
    list_display = (
        'title',
        'author',
        'created_date',
        'modified_date',
        'published_date',
    )
    fields = (
        'title',
        'text',
        'author',
        'published_date',
        ('created_date', 'modified_date'),
    )
    readonly_fields = (
        'created_date',
        'modified_date',
    )


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
