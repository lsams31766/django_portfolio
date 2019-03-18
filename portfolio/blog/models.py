from django.db import models

# Create blog model
# title 
# pub_date 
# body 
# image 
class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


# add blog app to the settings

# create a migration

# migrage

# add to admin 


