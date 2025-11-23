from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'topic', 'slug', 'created_by', 'created_at', 'updated_at']
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    list_display = ['title', 'short_text', 'topic']

    @admin.display(description='Short text')
    def short_text(self, obj):
        words = f'{obj.text}'.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'



# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post, PostAdmin)

