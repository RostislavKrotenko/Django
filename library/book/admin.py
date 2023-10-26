from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'description', 'name', 'count', 'date_of_issue', 'year_of_publication']
    search_fields = ['name']
    list_filter = ['id', 'name', 'author']
    readonly_fields = ()

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('name', 'author', 'year_of_publication')
        else:
            return self.readonly_fields

admin.site.register(Book, BookAdmin)
