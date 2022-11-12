from django import template
from blog.models import Post, Tag, Comments

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}


@register.inclusion_tag('blog/comments_tpl.html')
def get_comments():
    comments = Comments.objects.all()
    return {"comments": comments}
