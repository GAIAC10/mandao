#encoding: utf-8

# https://docs.djangoproject.com/en/2.0/howto/custom-management-commands/

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group,Permission,ContentType
from apps.cms.models import Vip,Company,Comment
from apps.mdmain.models import MdImg,MachineTime

class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1. 编辑组（管理新闻/管理课程/管理评论/管理轮播图等）
        edit_content_types = [
            ContentType.objects.get_for_model(MdImg),
            ContentType.objects.get_for_model(MachineTime),
            ContentType.objects.get_for_model(Company),
            ContentType.objects.get_for_model(Comment)
        ]
        edit_permissions = Permission.objects.filter(content_type__in=edit_content_types)
        editGroup = Group.objects.create(name='编辑')
        editGroup.permissions.set(edit_permissions)
        editGroup.save()
        self.stdout.write(self.style.SUCCESS('编辑组创建完成！'))

        # 2. 财务组（课程订roup单/付费资讯订单）
        finance_content_types = [
            ContentType.objects.get_for_model(Vip),
        ]
        finance_permissions = Permission.objects.filter(content_type__in=finance_content_types)
        financeGroup = Group.objects.create(name='财务')
        financeGroup.permissions.set(finance_permissions)
        financeGroup.save()
        self.stdout.write(self.style.SUCCESS('财务组创建完成！'))

        # 3. 管理员组（编辑组+财务组）
        admin_permissions = edit_permissions.union(finance_permissions)
        adminGroup = Group.objects.create(name='管理员')
        adminGroup.permissions.set(admin_permissions)
        adminGroup.save()
        # 4. 超级管理员
        self.stdout.write(self.style.SUCCESS('管理员组创建完成！'))