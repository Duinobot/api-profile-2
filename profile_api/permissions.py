from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    
    def has_object_permission(self,request,veiw,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.id == request.user.id