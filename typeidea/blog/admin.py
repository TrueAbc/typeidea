from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin
from .models import Post, Category, Tag
from .adminforms import PostAdminForm


# Register your models here.
class PostInline(admin.TabularInline):  # StackedInline 样式不同
    # 在分类界面编辑文章的内容
    fields = ('title', 'desc')
    extra = 1  # 额外控制多几个
    model = Post


class CategoryOwnerFilter(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户分类"""
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filetr(category_id=self.value())
        return queryset


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline, ]

    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count', 'id')
    fields = ('name', 'status', 'is_nav')
    list_filter = [CategoryOwnerFilter]

    #自定义展示字段
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # 配置该管理项目的表单
    form = PostAdminForm

    list_display = ('title', 'category', 'status',
                    'created_time', 'owner', 'operator', 'pv')
    list_display_links = []
    list_filter = ['category']
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # 编辑页面排除的字段
    exclude = ('owner', )

    # fields 以及 fieldsets 二者指定一个即可, 用来进行编辑页面的展示配置
    # fields = (('category', 'title'),
    #           'desc',
    #           'status',
    #           'content',
    #           'tag'
    #           )
    fieldsets = (
        ('基础配置', {
            'description': '基础配置信息描述',
            'fields': (
                ('title', 'category'),
                'status'
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            # 'classes': ('collapse',),
            'fields': ('tag',),
        })
    )
    filter_horizontal = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    # 自定义的media类来进行css以及js资源的加载
    class Media:
        css = {
            'all': ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css', ),
        }

        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js', )


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']

