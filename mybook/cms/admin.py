from django.contrib import admin
from cms.models import Book,Impression

# Register your models here.

# admin.site.register(Book)
# admin.site.register(Impression)

class BookAdmin(admin.ModelAdmin):
    list_display= ('id','name','publisher','page') #admin管理画面のBooksの画面一覧に表示したい項目
    list_display_links = ('id','name') #修正リンクでクリックできる項目


admin.site.register(Book,BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display= ('id','comment')
    list_display_links= ('id','comment')
    raw_id_fields= ('book',)#外部キーをプルダウンにしない（データ件数増加時のタイムアウトを予防）


admin.site.register(Impression,ImpressionAdmin)