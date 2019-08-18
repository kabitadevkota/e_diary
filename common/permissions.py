# from rest_framework import permissions
# from apis.accounts.models import Users

# class Is(permissions.BasePermission):

#     def has_permission(self,request,view):
#         users = request.users
#         grant_access = user.role in [role for role in dict(News.ROLES)]
#         #grant_access = str(user.role) in [role for role,value in User.ROLES if value in ['journalist','Admin']]
#         return grant_access