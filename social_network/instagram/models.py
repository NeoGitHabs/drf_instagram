from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    user_age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)], null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'follower:{self.follower} | following:{self.following}'

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hashtag = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} | image:{self.image} | video:{self.video} | description:{self.description} | hashtag:{self.hashtag}'

class PostLike(models.Model):
    user =  models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(blank=True, null=True,default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post',)

    def __str__(self):
        return f'user:{self.user} | post:{self.post} | like:{self.like}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} | post:{self.post} | text:{self.text} | parent:{self.parent}'

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment',)

    def __str__(self):
        return f'user:{self.user} | comment:{self.comment} | like:{self.like}'

class Story(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='story_images/', blank=True, null=True)
    video = models.FileField(upload_to='story_videos/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'user:{self.user} | image:{self.image} | video:{self.video}'

class Save(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'user:{self.user}'

class SaveItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    save = models.IntegerField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'post:{self.post} | save:{self.save}'

#+ .env
#+ translate(+2)
#+ pagination
#+ swagger
#+ filter(hashtag), search(username), order(post(created_at))
# permission
# jwt


