from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_posts",
        # I want to make the users see the post of a
        # deleted user
        on_delete=models.SET_NULL,
        null=True
    )
    group = models.ForeignKey(
        "share.Group",
        on_delete=models.SET_NULL,
        null=True,
        related_name="group_posts"
    )
    title = models.CharField(
        "Title of the post",
        max_length=100  
    )
    title_slug = models.SlugField(
        "title slug",
        unique=True
    )
    # has no use for now
    is_archived = models.BooleanField(
        default=False
    )
    # for now users could only post texts
    text_content = models.TextField()
    post_at = models.DateField(
        auto_now_add=True
    )
    # TODO: add liking system on posts 
    # TODO: add post history of edits
    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(self.title) 

            try:
                count = self.objects.filter(
                    title_slug=slug,
                    group=self.group
                ).count()

                self.title_slug = f"{slug}_{count+1}"

            except Post.DoesNotExist:
                self.title_slug = slug

        super(Post, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title_slug

    def get_absolute_url(self):
        # the path of the post should be:
        # g/post slug/
        return NotImplementedError
