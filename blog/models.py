from django.db import models

class RcentBlog(models.Model):
    # class Month(models.TextChoices):    
    #     jan = "January", "Jan"
    #     feb = "February","Fab"
    #     march = "March","March"
    #     april = "April","April"
    #     may = "May","May"
    #     june = "June","June"
    #     july = "July", "July"
    #     aug = "August", "Aug"
    #     sep = "September","Sep"
    #     oct = "October","Oct"
    #     nov = "November","Nov"
    #     dec = "December","Dec"
      
    
    # month = models.CharField(max_length=10,choices=Month.choices, default=Month.dec)    
    title = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/recent_blog/')
    def __str__(self):
        return self.title
