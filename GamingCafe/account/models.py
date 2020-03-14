from django.db import models
from membership.models import Membership
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from package.models import Package




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_left = models.PositiveIntegerField(default=0)
    total_time = models.PositiveIntegerField(default=0)
    membership_status = models.ForeignKey(
        Membership, on_delete=models.CASCADE, default='The Warrior')
    join_date = models.DateTimeField()

    def __str__(self):
        return str(self.user.username)

    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            user_profile = UserProfile(user=user, join_date=timezone.now())
            user_profile.save()

    post_save.connect(create_profile, sender=User)


class Receipt(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField()
    mrp = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    amount = models.FloatField()

    def __str__(self):
        return str(self.user)


def package_bought(sender, **kwargs):
        receipt = kwargs["instance"]
        if kwargs['created']:
            userprofile = receipt.user
            package = receipt.package
            userprofile.total_time = userprofile.total_time + package.time_added
            userprofile.time_left = userprofile.time_left + package.time_added
            if(userprofile.total_time > 100 and userprofile.total_time <= 500 and userprofile.membership_status != 'The Mage'):
                membership = Membership.objects.get(rank='The Mage')
                userprofile.membership_status = membership
            elif(userprofile.total_time > 500 and userprofile.total_time <= 5000 and userprofile.membership_status != 'The Knight'):
                membership = Membership.objects.get(rank='The Knight')
                userprofile.membership_status = membership
            elif(userprofile.total_time > 5000 and userprofile.membership_status != 'The Withcer'):
                membership = Membership.objects.get(rank='The Witcher')
                userprofile.membership_status = membership
            userprofile.save()

post_save.connect(package_bought,sender=Receipt)
