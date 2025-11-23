from django.contrib import admin
from .models import Category, Topic, Post


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'topic', 'slug', 'created_by', 'created_at', 'updated_at']
    readonly_fields = ['created_by', 'created_at', 'updated_at']
    list_display = ['title', 'short_text', 'topic', 'topic_category', 'created_at']
    # kolumny klikalne - przejście do szczegółów wiersza
    list_display_links = ['title', 'short_text']
    # zapis topic__category__name jest wymagany, aby można było przez nazwę
    # kolumny w postaci łańcucha znaków (typ str) przekazać wartość równoważną
    # wywołaniu topic.category.name
    list_filter = ['topic', 'topic__category__name', 'created_by']
    prepopulated_fields = {'slug': ['title']}

    @admin.display(description='Short text')
    def short_text(self, obj):
        words = f'{obj.text}'.split()
        if len(words) <= 5:
            return ' '.join(words)
        else:
            return ' '.join(words[:5]) + ' ...'

    @admin.display(description='Topic (category)')
    def topic_category(self, obj):
        return f'{obj.topic.name} ({obj.topic.category.name})'


class TopicAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ['name', 'category', 'topic_category', 'created']

    @admin.display(description='Topic (category)')
    def topic_category(self, obj):
        return f'{obj.name} ({obj.category.name})'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

# a następnie zarejestrować (pokazano najprostszy przypadek)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)

