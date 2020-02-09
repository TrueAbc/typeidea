import xadmin

from django.utils.html import format_html
from xadmin.filters import RelatedFieldListFilter, manager

from xadmin.layout import Row, Fieldset, Container

from typeidea.base_admin import BaseOwnerAdmin
from .models import Post, Category, Tag
from .adminforms import PostAdminForm


# Register your models here.
class PostInline:  # StackedInline 样式不同
    # 在分类界面编辑文章的内容
    form_layout = (
        Container(
            Row('title', 'desc')
        )
    )
    extra = 1  # 额外控制多几个
    model = Post


class CategoryOwnerFilter(RelatedFieldListFilter):
    """自定义过滤器只展示当前用户分类"""

    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(CategoryOwnerFilter, self).__init__(field, request, params, model, model_admin, field_path)
        # 重新获取lookup_choiced，根据owner过滤
        self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]

    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count', 'id')
    fields = ('name', 'status', 'is_nav')

    # 自定义展示字段
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    # 配置该管理项目的表单
    form = PostAdminForm

    list_filter = ['category']  # 这里不是定义的filter类，是字段名字

    list_display = ('title', 'category', 'status',
                    'created_time', 'owner', 'operator', 'pv')
    list_display_links = []
    search_fields = ['title', 'category__name']

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'status',
        ),
        Fieldset(
            '内容信息',
            'desc',
            'is_md',
            'content_ck',
            'content_md',
            'content',
        )
    )

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True

    # 编辑页面排除的字段
    exclude = ('owner', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            self.model_admin_url('change', obj.id)
        )

    operator.short_description = '操作'
